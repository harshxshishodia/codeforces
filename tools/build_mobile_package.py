#!/usr/bin/env python3
"""Build deterministic Codeforces mobile content from contest folders."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse

from validate_content import APPROACH_DIRECTORY, Contest, Problem, metadata, validate


SEED_ROOT_NAME = "codeforces_seed"
MARKDOWN_IMAGE = re.compile(
    r"!\[(?P<alt>[^\]]*)]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"].*?['\"])?\)"
)
HTML_IMAGE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*['\"](?P<target>[^'\"]+)['\"][^>]*>",
    re.IGNORECASE,
)
NON_SLUG = re.compile(r"[^a-z0-9]+")
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
LANGUAGE_BY_SUFFIX = {
    ".c": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".cxx": "cpp",
    ".go": "go",
    ".java": "java",
    ".js": "javascript",
    ".kt": "kotlin",
    ".kts": "kotlin",
    ".py": "python",
    ".py3": "python3",
    ".rb": "ruby",
    ".rs": "rust",
    ".swift": "swift",
    ".ts": "typescript",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slugify(value: str) -> str:
    return NON_SLUG.sub("-", value.lower()).strip("-") or "problem"


def source_version(root: Path, contests: list[Contest]) -> str:
    configured = os.environ.get("GITHUB_SHA", "").strip()
    if configured:
        return configured
    try:
        value = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if value:
            return value
    except (OSError, subprocess.CalledProcessError):
        pass
    digest = hashlib.sha256()
    for contest in contests:
        for problem in contest.problems:
            digest.update(problem.readme.relative_to(root).as_posix().encode())
            digest.update(problem.readme.read_bytes())
    return f"local-{digest.hexdigest()[:24]}"


def trim_readme_header(text: str) -> str:
    lines = text.replace("\r\n", "\n").splitlines()
    first_heading = next(
        (index for index, line in enumerate(lines) if line.strip().startswith("# ")),
        None,
    )
    if first_heading is not None:
        lines[first_heading] = ""
    first_section = next(
        (index for index, line in enumerate(lines) if line.strip().startswith("## ")),
        None,
    )
    if first_section is not None:
        lines = lines[first_section:]
    return "\n".join(lines).strip()


def image_spans(text: str):
    spans = []
    for match in MARKDOWN_IMAGE.finditer(text):
        spans.append(
            (
                match.start(),
                match.end(),
                match.group("target").strip("<>"),
                match.group("alt") or "Problem image",
            )
        )
    for match in HTML_IMAGE.finditer(text):
        spans.append(
            (
                match.start(),
                match.end(),
                match.group("target"),
                "Problem image",
            )
        )
    return sorted(spans, key=lambda value: value[0])


def resolve_local_image(root: Path, readme: Path, target: str) -> Path | None:
    parsed = urlparse(target.strip("<>"))
    if parsed.scheme or target.startswith("//") or not parsed.path:
        return None
    candidate = (readme.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def add_text_block(blocks: list[dict], text: str) -> None:
    normalized = text.strip()
    if normalized:
        blocks.append({"type": "text", "text": normalized})


def build_content(
    root: Path,
    seed_root: Path,
    problem: Problem,
) -> tuple[list[dict], list[dict]]:
    statement = trim_readme_header(problem.readme.read_text(encoding="utf-8"))
    destination = (
        seed_root
        / "assets"
        / f"{problem.contest_id:04d}"
        / f"{problem.index.lower()}-{slugify(problem.name)}"
    )
    blocks: list[dict] = []
    assets: list[dict] = []
    cursor = 0
    used_names: set[str] = set()
    for start, end, target, alt in image_spans(statement):
        if start < cursor:
            continue
        image = resolve_local_image(root, problem.readme, target)
        if image is None:
            continue
        add_text_block(blocks, statement[cursor:start])
        safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", image.name).strip("-") or "image"
        if safe_name.casefold() in used_names:
            safe_name = (
                f"{Path(safe_name).stem}-{sha256_file(image)[:10]}"
                f"{Path(safe_name).suffix}"
            )
        used_names.add(safe_name.casefold())
        destination.mkdir(parents=True, exist_ok=True)
        copied = destination / safe_name
        shutil.copyfile(image, copied)
        data = copied.read_bytes()
        relative = copied.relative_to(seed_root.parent).as_posix()
        asset = {
            "bytes": len(data),
            "contentType": mimetypes.guess_type(copied.name)[0]
            or "application/octet-stream",
            "localPath": relative,
            "originalUrl": target,
            "sha256": sha256_bytes(data),
        }
        assets.append(asset)
        blocks.append(
            {
                "type": "image",
                "alt": alt,
                "localPath": relative,
                "sha256": asset["sha256"],
                "contentType": asset["contentType"],
            }
        )
        cursor = end
    add_text_block(blocks, statement[cursor:])
    if not blocks:
        add_text_block(blocks, statement)
    for index, block in enumerate(blocks):
        block["sequence"] = index
    return blocks, assets


def read_approaches(problem: Problem) -> list[dict]:
    grouped: dict[int, dict[str, dict]] = {}
    directories = []
    for directory in problem.directory.iterdir():
        match = APPROACH_DIRECTORY.fullmatch(directory.name) if directory.is_dir() else None
        if match is not None:
            directories.append(
                (
                    int(match.group("number")),
                    0 if directory.name.lower().startswith("approach") else 1,
                    directory,
                )
            )
    for number, _, directory in sorted(
        directories,
        key=lambda item: (item[0], item[1], item[2].name.casefold()),
    ):
        solutions = grouped.setdefault(number, {})
        for source in sorted(directory.iterdir(), key=lambda path: path.name.casefold()):
            if not source.is_file():
                continue
            language = LANGUAGE_BY_SUFFIX.get(source.suffix.lower())
            if language is None:
                continue
            solutions.setdefault(
                language,
                {
                    "language": language,
                    "fileName": source.name,
                    "code": source.read_text(encoding="utf-8").strip(),
                },
            )
    return [
        {
            "number": number,
            "label": f"Approach {number}",
            "solutions": [
                values[language]
                for language in sorted(values)
            ],
        }
        for number, values in sorted(grouped.items())
    ]


def split_limits(value: str) -> tuple[str, str]:
    parts = [part.strip() for part in value.split("/", 1)]
    return (
        parts[0] if parts else "",
        parts[1] if len(parts) > 1 else "",
    )


def build_problem(root: Path, seed_root: Path, problem: Problem) -> dict:
    raw = problem.readme.read_text(encoding="utf-8")
    tags_value = metadata(raw, "Tags") or metadata(raw, "Topics")
    tags = [tag.strip().lower() for tag in tags_value.split(",") if tag.strip()]
    time_limit, memory_limit = split_limits(metadata(raw, "Limits"))
    blocks, assets = build_content(root, seed_root, problem)
    rating_value = metadata(raw, "Rating").lstrip("*").strip()
    return {
        "problemKey": problem.key,
        "contestId": problem.contest_id,
        "index": problem.index,
        "name": problem.name,
        "url": metadata(raw, "Submission")
        or f"https://codeforces.com/contest/{problem.contest_id}/problem/{problem.index}",
        "timeLimit": time_limit,
        "memoryLimit": memory_limit,
        "rating": int(rating_value) if rating_value.isdigit() else None,
        "tags": list(dict.fromkeys(tags)),
        "contentBlocks": blocks,
        "assets": assets,
        "approaches": read_approaches(problem),
    }


def write_json(path: Path, value: object) -> bytes:
    data = (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def write_deterministic_zip(source: Path, destination: Path) -> None:
    with zipfile.ZipFile(
        destination,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in sorted(
            source.rglob("*"),
            key=lambda item: item.relative_to(source).as_posix(),
        ):
            if not path.is_file():
                continue
            info = zipfile.ZipInfo(
                path.relative_to(source).as_posix(),
                FIXED_ZIP_TIME,
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)


def build(
    content_root: Path,
    output: Path,
    version: str | None,
    generated_at: str | None,
    contest_id: int | None = None,
) -> None:
    content_root = content_root.resolve()
    output = output.resolve()
    contests, errors = validate(content_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    if contest_id is not None:
        contests = [contest for contest in contests if contest.contest_id == contest_id]
        if not contests:
            raise SystemExit(f"Contest {contest_id} was not found")
    content_version = version or source_version(content_root, contests)
    timestamp = generated_at or (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    staging = output.parent / f".{output.name}-staging"
    shutil.rmtree(staging, ignore_errors=True)
    staging.mkdir(parents=True)
    package_tree = staging / "package"
    seed_root = package_tree / SEED_ROOT_NAME
    batches = []
    problem_count = 0
    for contest in contests:
        problems = [
            build_problem(content_root, seed_root, problem)
            for problem in contest.problems
        ]
        problem_count += len(problems)
        relative = f"contests/{contest.contest_id:04d}.json"
        data = write_json(
            seed_root / relative,
            {
                "schemaVersion": 1,
                "contest": {
                    "id": contest.contest_id,
                    "name": contest.name,
                    "range": contest.range_name,
                    "url": f"https://codeforces.com/contest/{contest.contest_id}",
                },
                "problems": problems,
            },
        )
        batches.append(
            {
                "contestId": contest.contest_id,
                "file": relative,
                "sha256": sha256_bytes(data),
                "size": len(data),
            }
        )
    write_json(
        seed_root / "manifest.json",
        {
            "schemaVersion": 1,
            "generatedAt": timestamp,
            "contestCount": len(contests),
            "problemCount": problem_count,
            "batches": batches,
        },
    )
    package_file = staging / "content-package.zip"
    write_deterministic_zip(package_tree, package_file)
    package_hash = sha256_file(package_file)
    published_files = []
    for path in sorted(
        package_tree.rglob("*"),
        key=lambda item: item.relative_to(package_tree).as_posix(),
    ):
        if not path.is_file():
            continue
        relative = path.relative_to(package_tree).as_posix()
        file_hash = sha256_file(path)
        destination = staging / "objects" / file_hash
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            shutil.copyfile(path, destination)
        published_files.append(
            {
                "path": relative,
                "file": f"objects/{file_hash}",
                "sha256": file_hash,
                "size": path.stat().st_size,
            }
        )
    manifest_data = write_json(
        staging / "manifest.json",
        {
            "schemaVersion": 1,
            "contentVersion": content_version,
            "generatedAt": timestamp,
            "packageFile": "content-package.zip",
            "packageSha256": package_hash,
            "packageSize": package_file.stat().st_size,
            "files": published_files,
        },
    )
    (staging / "checksums.sha256").write_text(
        f"{package_hash}  content-package.zip\n"
        f"{sha256_bytes(manifest_data)}  manifest.json\n",
        encoding="utf-8",
        newline="\n",
    )
    shutil.rmtree(package_tree)
    shutil.rmtree(output, ignore_errors=True)
    staging.replace(output)
    print(
        f"Built {output / 'content-package.zip'} "
        f"({len(contests)} contests, {problem_count} problems)"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--content-version")
    parser.add_argument("--generated-at")
    parser.add_argument("--contest-id", type=int)
    args = parser.parse_args()
    build(
        content_root=args.content_root,
        output=args.output
        or args.content_root / "generated-mobile-content",
        version=args.content_version,
        generated_at=args.generated_at,
        contest_id=args.contest_id,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
