#!/usr/bin/env python3
"""Create missing problem folders (with minimal README.md) for empty contest folders.

For contest folders that have no valid problem subdirectories, fetches the
problem list from the Codeforces API (or falls back to HTML scraping) and creates:
  <contest_folder>/<INDEX> - <Problem Name>/README.md

The README contains only the minimum required by validate_content.py:
  # <INDEX>. <Problem Name>
  **Submission:** https://codeforces.com/contest/<id>/problem/<INDEX>
"""

from __future__ import annotations

import html as html_module
import io
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RANGE_DIRECTORY = re.compile(r"^\d+-\d+$")
CONTEST_DIRECTORY = re.compile(r"^(?P<id>[1-9]\d*)\s*-\s*(?P<name>.+)$")
PROBLEM_DIRECTORY = re.compile(r"^(?P<index>[A-Za-z][A-Za-z0-9]*)\s*-\s*(?P<name>.+)$")
IGNORED = {".git", ".github", ".idea", ".vscode", "__pycache__", "generated-mobile-content"}

CF_API = "https://codeforces.com/api/contest.standings?contestId={cid}&from=1&count=1"
CF_PROBLEMS_PAGE = "https://codeforces.com/contest/{cid}/problems"


def _get_url(url: str) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"    [fetch error] {url}: {e}")
        return None


def fetch_via_api(contest_id: str) -> list[dict] | None:
    url = CF_API.format(cid=contest_id)
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        if data.get("status") == "OK":
            return data["result"]["problems"]
    except Exception:
        pass
    return None


def fetch_via_scrape(contest_id: str) -> list[dict] | None:
    """Scrape /contest/{id}/problems to extract problem index + name pairs."""
    html = _get_url(CF_PROBLEMS_PAGE.format(cid=contest_id))
    if not html:
        return None

    # Codeforces problems table structure (simplified):
    #   <td class="id"><a href="/contest/ID/problem/A">A</a></td>
    #   <td><div ...><a href="/contest/ID/problem/A">Problem Name</a></div></td>
    # Strategy: find href="/contest/.../problem/INDEX" with link text != INDEX
    pattern = re.compile(
        r'href="/contest/\d+/problem/([A-Za-z][A-Za-z0-9]*)">([^<]+)</a>',
        re.IGNORECASE,
    )
    seen: dict[str, str] = {}
    for m in pattern.finditer(html):
        index = m.group(1).strip().upper()
        name = html_module.unescape(m.group(2).strip())
        # The index-cell link has text == index; skip those
        if name.upper() == index:
            continue
        if len(name) < 2 or len(name) > 300:
            continue
        if index not in seen:
            seen[index] = name

    if seen:
        return [{"index": idx, "name": nm} for idx, nm in sorted(seen.items())]
    return None


def fetch_problems(contest_id: str) -> list[dict] | None:
    result = fetch_via_api(contest_id)
    if result:
        return result
    time.sleep(0.3)
    result = fetch_via_scrape(contest_id)
    return result


# Sanitize characters that are invalid in Windows folder names
_INVALID_WIN = re.compile(r'[\\/:*?"<>|]')


def safe_name(name: str) -> str:
    return _INVALID_WIN.sub("-", name).strip()


def fix_empty_contests(root: Path) -> None:
    fixed = 0
    skipped = 0

    for range_path in sorted(root.iterdir()):
        if not range_path.is_dir() or range_path.name in IGNORED:
            continue
        if not RANGE_DIRECTORY.fullmatch(range_path.name):
            continue

        for contest_path in sorted(range_path.iterdir()):
            if not contest_path.is_dir():
                continue
            contest_match = CONTEST_DIRECTORY.fullmatch(contest_path.name)
            if not contest_match:
                continue

            # Check if the contest already has valid problem subdirs
            has_problems = any(
                PROBLEM_DIRECTORY.fullmatch(p.name)
                for p in contest_path.iterdir()
                if p.is_dir()
            )
            if has_problems:
                skipped += 1
                continue

            contest_id = contest_match.group("id")
            print(f"  Fetching problems for contest {contest_id} ...")
            problems = fetch_problems(contest_id)
            time.sleep(0.3)  # be polite to the API

            if not problems:
                print(f"    [skip] No problems returned for contest {contest_id}")
                continue

            for prob in problems:
                index = prob.get("index", "").strip().upper()
                name = prob.get("name", "").strip()
                if not index or not name:
                    continue
                folder_name = f"{index} - {safe_name(name)}"
                problem_path = contest_path / folder_name
                problem_path.mkdir(exist_ok=True)
                readme = problem_path / "README.md"
                if not readme.exists():
                    url = f"https://codeforces.com/contest/{contest_id}/problem/{index}"
                    content = f"# {index}. {name}\n\n**Submission:** {url}\n"
                    readme.write_text(content, encoding="utf-8")
                    print(f"    Created: {readme.relative_to(root)}")
                    fixed += 1

    print(f"\nDone: {fixed} new README.md files created, {skipped} contests already had problems.")


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
    print(f"Scanning: {root}\n")
    fix_empty_contests(root)
