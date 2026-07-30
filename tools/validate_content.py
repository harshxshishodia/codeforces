#!/usr/bin/env python3
"""Validate a contest-wise Codeforces content repository without modifying it."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


RANGE_DIRECTORY = re.compile(r"^(?P<start>\d+)-(?P<end>\d+)$")
CONTEST_DIRECTORY = re.compile(r"^(?P<id>[1-9]\d*)\s*-\s*(?P<name>.+)$")
PROBLEM_DIRECTORY = re.compile(
    r"^(?P<index>[A-Za-z][A-Za-z0-9]*)\s*-\s*(?P<name>.+)$"
)
APPROACH_DIRECTORY = re.compile(
    r"^(?:Approach|Solution)\s+(?P<number>[1-9]\d*)$",
    re.IGNORECASE,
)
MARKDOWN_IMAGE = re.compile(
    r"!\[(?P<alt>[^\]]*)]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"].*?['\"])?\)"
)
HTML_IMAGE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*['\"](?P<target>[^'\"]+)['\"][^>]*>",
    re.IGNORECASE,
)
SOURCE_SUFFIXES = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".cxx",
    ".go",
    ".java",
    ".js",
    ".kt",
    ".kts",
    ".py",
    ".py3",
    ".rb",
    ".rs",
    ".swift",
    ".ts",
}
IGNORED_DIRECTORIES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    "generated-mobile-content",
}


@dataclass(frozen=True)
class Problem:
    contest_id: int
    contest_name: str
    range_name: str
    index: str
    name: str
    directory: Path
    readme: Path

    @property
    def key(self) -> str:
        return f"{self.contest_id}-{self.index.upper()}"


@dataclass(frozen=True)
class Contest:
    contest_id: int
    name: str
    range_name: str
    directory: Path
    problems: tuple[Problem, ...]


class Validation:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.errors: list[str] = []
        self.contests: list[Contest] = []

    def error(self, path: Path, reason: str) -> None:
        try:
            display = path.resolve(strict=False).relative_to(self.root).as_posix()
        except ValueError:
            display = str(path)
        self.errors.append(f"{display}: {reason}")

    def run(self) -> list[Contest]:
        if not self.root.is_dir():
            self.error(self.root, "content root does not exist or is not a directory")
            return []
        self._validate_case_conflicts()
        self._discover_contests()
        return sorted(self.contests, key=lambda contest: contest.contest_id)

    def _source_files(self):
        for path in self.root.rglob("*"):
            relative = path.relative_to(self.root)
            if any(part in IGNORED_DIRECTORIES for part in relative.parts):
                continue
            if path.is_file():
                yield path

    def _validate_case_conflicts(self) -> None:
        seen: dict[str, Path] = {}
        for path in self._source_files():
            relative = path.relative_to(self.root).as_posix()
            previous = seen.get(relative.casefold())
            if previous is not None and previous != path:
                self.error(
                    path,
                    f"case-sensitive path conflict with "
                    f"{previous.relative_to(self.root).as_posix()}",
                )
            else:
                seen[relative.casefold()] = path

    def _discover_contests(self) -> None:
        ranges = [
            path
            for path in self.root.iterdir()
            if path.is_dir() and RANGE_DIRECTORY.fullmatch(path.name)
        ]
        if not ranges:
            self.error(self.root, "no contest ranges such as 0001-0100 were found")
            return
        seen_contests: dict[int, Path] = {}
        seen_problem_keys: dict[str, Path] = {}
        for range_path in sorted(ranges, key=lambda path: range_bounds(path.name)):
            bounds = range_bounds(range_path.name)
            for contest_path in sorted(
                (path for path in range_path.iterdir() if path.is_dir()),
                key=lambda path: contest_sort_key(path.name),
            ):
                contest_match = CONTEST_DIRECTORY.fullmatch(contest_path.name)
                if contest_match is None:
                    self.error(
                        contest_path,
                        "contest folder must be '<id> - <contest name>'",
                    )
                    continue
                contest_id = int(contest_match.group("id"))
                if not bounds[0] <= contest_id <= bounds[1]:
                    self.error(
                        contest_path,
                        f"contest {contest_id} is outside range {range_path.name}",
                    )
                previous = seen_contests.get(contest_id)
                if previous is not None:
                    self.error(
                        contest_path,
                        f"duplicate contest ID {contest_id}; first found at "
                        f"{previous.relative_to(self.root)}",
                    )
                else:
                    seen_contests[contest_id] = contest_path
                problems = self._discover_problems(
                    range_path,
                    contest_path,
                    contest_id,
                    contest_match.group("name").strip(),
                    seen_problem_keys,
                )
                if not problems:
                    self.error(contest_path, "contest contains no problem folders")
                self.contests.append(
                    Contest(
                        contest_id=contest_id,
                        name=contest_match.group("name").strip(),
                        range_name=range_path.name,
                        directory=contest_path,
                        problems=tuple(problems),
                    )
                )

    def _discover_problems(
        self,
        range_path: Path,
        contest_path: Path,
        contest_id: int,
        contest_name: str,
        seen_problem_keys: dict[str, Path],
    ) -> list[Problem]:
        problems: list[Problem] = []
        seen_indices: set[str] = set()
        for problem_path in sorted(
            (path for path in contest_path.iterdir() if path.is_dir()),
            key=lambda path: problem_index_sort_key(path.name),
        ):
            problem_match = PROBLEM_DIRECTORY.fullmatch(problem_path.name)
            if problem_match is None:
                self.error(
                    problem_path,
                    "problem folder must be '<index> - <problem name>'",
                )
                continue
            index = problem_match.group("index").upper()
            if index.casefold() in seen_indices:
                self.error(problem_path, f"duplicate problem index {index}")
            seen_indices.add(index.casefold())
            key = f"{contest_id}-{index}"
            previous = seen_problem_keys.get(key.casefold())
            if previous is not None:
                self.error(
                    problem_path,
                    f"duplicate problem key {key}; first found at "
                    f"{previous.relative_to(self.root)}",
                )
            else:
                seen_problem_keys[key.casefold()] = problem_path
            readme = problem_path / "README.md"
            if not readme.is_file():
                self.error(problem_path, "missing required README.md")
                continue
            problem = Problem(
                contest_id=contest_id,
                contest_name=contest_name,
                range_name=range_path.name,
                index=index,
                name=problem_match.group("name").strip(),
                directory=problem_path,
                readme=readme,
            )
            self._validate_readme(problem)
            self._validate_approaches(problem)
            problems.append(problem)
        return problems

    def _read_utf8(self, path: Path) -> str | None:
        try:
            data = path.read_bytes()
        except OSError as error:
            self.error(path, f"file cannot be read: {error}")
            return None
        if not data:
            self.error(path, "required file is empty")
            return None
        try:
            return data.decode("utf-8-sig")
        except UnicodeDecodeError as error:
            self.error(path, f"unsupported encoding; expected UTF-8: {error}")
            return None

    def _validate_readme(self, problem: Problem) -> None:
        text = self._read_utf8(problem.readme)
        if text is None:
            return
        heading = re.search(
            r"^#\s+(?P<index>[A-Za-z][A-Za-z0-9]*)[.)]\s+(?P<name>.+?)\s*$",
            text,
            re.MULTILINE,
        )
        if heading is None:
            self.error(problem.readme, "missing '# <index>. <problem name>' heading")
        elif heading.group("index").upper() != problem.index:
            self.error(
                problem.readme,
                f"heading index {heading.group('index')} does not match {problem.index}",
            )
        submission = metadata(text, "Submission")
        if not submission:
            self.error(problem.readme, "missing Submission metadata")
        elif f"/{problem.contest_id}/problem/{problem.index}" not in submission:
            self.error(
                problem.readme,
                "Submission URL does not match the contest and problem index",
            )
        for target in image_targets(text):
            self._validate_image(problem.readme, target)

    def _validate_image(self, readme: Path, target: str) -> None:
        parsed = urlparse(target.strip("<>"))
        if parsed.scheme.lower() in {"http", "https", "data"} or target.startswith("//"):
            return
        if parsed.scheme:
            self.error(readme, f"unsupported image reference scheme: {target}")
            return
        resolved = (readme.parent / unquote(parsed.path)).resolve(strict=False)
        try:
            resolved.relative_to(self.root)
        except ValueError:
            self.error(readme, f"image reference escapes content root: {target}")
            return
        if not resolved.is_file():
            self.error(readme, f"missing referenced image: {target}")

    def _validate_approaches(self, problem: Problem) -> None:
        seen: set[int] = set()
        for directory in (path for path in problem.directory.iterdir() if path.is_dir()):
            match = APPROACH_DIRECTORY.fullmatch(directory.name)
            if match is None:
                if directory.name.lower() != "images":
                    self.error(
                        directory,
                        "subfolder must be images, Approach N, or Solution N",
                    )
                continue
            number = int(match.group("number"))
            if number in seen and directory.name.lower().startswith("approach"):
                self.error(directory, f"duplicate approach number {number}")
            seen.add(number)
            for source in (path for path in directory.iterdir() if path.is_file()):
                if source.suffix.lower() not in SOURCE_SUFFIXES:
                    continue
                try:
                    source.read_text(encoding="utf-8")
                except UnicodeDecodeError as error:
                    self.error(source, f"solution source must be UTF-8: {error}")


def metadata(text: str, name: str) -> str:
    match = re.search(
        rf"^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$",
        text,
        re.MULTILINE | re.IGNORECASE,
    )
    return match.group(1).strip() if match else ""


def image_targets(text: str):
    for match in MARKDOWN_IMAGE.finditer(text):
        yield match.group("target").strip("<>")
    for match in HTML_IMAGE.finditer(text):
        yield match.group("target")


def range_bounds(value: str) -> tuple[int, int]:
    match = RANGE_DIRECTORY.fullmatch(value)
    if match is None:
        return (sys.maxsize, sys.maxsize)
    return int(match.group("start")), int(match.group("end"))


def contest_sort_key(value: str) -> tuple[int, str]:
    match = CONTEST_DIRECTORY.fullmatch(value)
    return (int(match.group("id")), value) if match else (sys.maxsize, value)


def problem_index_sort_key(value: str) -> tuple[str, int, str]:
    match = PROBLEM_DIRECTORY.fullmatch(value)
    if match is None:
        return (value, sys.maxsize, value)
    index = match.group("index").upper()
    letters = "".join(character for character in index if character.isalpha())
    digits = "".join(character for character in index if character.isdigit())
    return letters, int(digits or 0), value


def validate(root: Path) -> tuple[list[Contest], list[str]]:
    validation = Validation(root)
    return validation.run(), validation.errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    contests, errors = validate(args.content_root)
    if errors:
        print(f"Content validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    problem_count = sum(len(contest.problems) for contest in contests)
    print(
        f"Content validation passed: {len(contests)} contests, "
        f"{problem_count} problems"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
