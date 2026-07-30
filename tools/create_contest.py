#!/usr/bin/env python3
"""Create a Codeforces contest and problem README/approach folders."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PROBLEM_VALUE = re.compile(
    r"^(?P<index>[A-Za-z][A-Za-z0-9]*)\s*:\s*(?P<name>.+)$"
)


def contest_range(contest_id: int) -> str:
    start = ((contest_id - 1) // 100) * 100 + 1
    return f"{start:04d}-{start + 99:04d}"


def create_contest(
    root: Path,
    contest_id: int,
    contest_name: str,
    problems: list[str],
    approach_count: int,
) -> Path:
    contest = (
        root
        / contest_range(contest_id)
        / f"{contest_id} - {contest_name.strip()}"
    )
    contest.mkdir(parents=True, exist_ok=True)
    for value in problems:
        match = PROBLEM_VALUE.fullmatch(value)
        if match is None:
            raise ValueError(
                f"Invalid problem {value!r}; use INDEX:Problem name"
            )
        index = match.group("index").upper()
        name = match.group("name").strip()
        problem = contest / f"{index} - {name}"
        problem.mkdir(parents=True, exist_ok=True)
        readme = problem / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# {index}. {name}\n\n"
                f"**Submission:** "
                f"https://codeforces.com/contest/{contest_id}/problem/{index}\n\n"
                "**Limits:** \n\n"
                "**Rating:** \n\n"
                "**Tags:** \n\n"
                "## Problem Statement\n\n"
                "## Input\n\n"
                "## Output\n\n"
                "## Examples\n",
                encoding="utf-8",
                newline="\n",
            )
        images = problem / "images"
        images.mkdir(exist_ok=True)
        (images / ".gitkeep").touch(exist_ok=True)
        for number in range(1, approach_count + 1):
            approach = problem / f"Approach {number}"
            approach.mkdir(exist_ok=True)
            source = approach / "main.cpp"
            source.touch(exist_ok=True)
    return contest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", type=Path, default=Path.cwd())
    parser.add_argument("--contest", type=int, required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument(
        "--problem",
        action="append",
        required=True,
        help="Repeat as --problem A:Problem name",
    )
    parser.add_argument("--approaches", type=int, default=1)
    args = parser.parse_args()
    if args.contest <= 0:
        parser.error("--contest must be positive")
    if args.approaches <= 0:
        parser.error("--approaches must be positive")
    contest = create_contest(
        root=args.content_root.resolve(),
        contest_id=args.contest,
        contest_name=args.name,
        problems=args.problem,
        approach_count=args.approaches,
    )
    print(f"Created {contest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
