#!/usr/bin/env python3
"""Generate minimal README.md files for problem folders that are missing them.

The README contains only the minimum required by validate_content.py:
  - A heading:       # <INDEX>. <Problem Name>
  - A submission:    **Submission:** https://codeforces.com/contest/<id>/problem/<INDEX>
"""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

# Force UTF-8 output on Windows so non-ASCII folder names don't crash print()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RANGE_DIRECTORY = re.compile(r"^\d+-\d+$")
CONTEST_DIRECTORY = re.compile(r"^(?P<id>[1-9]\d*)\s*-\s*(?P<name>.+)$")
PROBLEM_DIRECTORY = re.compile(r"^(?P<index>[A-Za-z][A-Za-z0-9]*)\s*-\s*(?P<name>.+)$")

IGNORED = {".git", ".github", ".idea", ".vscode", "__pycache__", "generated-mobile-content"}


def generate(root: Path) -> None:
    created = 0
    skipped = 0

    for range_path in sorted(root.iterdir()):
        if not range_path.is_dir():
            continue
        if range_path.name in IGNORED:
            continue
        if not RANGE_DIRECTORY.fullmatch(range_path.name):
            continue

        for contest_path in sorted(range_path.iterdir()):
            if not contest_path.is_dir():
                continue
            contest_match = CONTEST_DIRECTORY.fullmatch(contest_path.name)
            if not contest_match:
                continue
            contest_id = contest_match.group("id")

            for problem_path in sorted(contest_path.iterdir()):
                if not problem_path.is_dir():
                    continue
                problem_match = PROBLEM_DIRECTORY.fullmatch(problem_path.name)
                if not problem_match:
                    continue

                readme = problem_path / "README.md"
                if readme.exists():
                    skipped += 1
                    continue

                index = problem_match.group("index").upper()
                name = problem_match.group("name").strip()
                url = f"https://codeforces.com/contest/{contest_id}/problem/{index}"

                content = f"# {index}. {name}\n\n**Submission:** {url}\n"
                readme.write_text(content, encoding="utf-8")
                print(f"  Created: {readme.relative_to(root)}")
                created += 1

    print(f"\nDone: {created} README.md files created, {skipped} already existed.")


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
    print(f"Scanning: {root}\n")
    generate(root)
