from __future__ import annotations

import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from build_mobile_package import build, sha256_file  # noqa: E402
from create_contest import create_contest  # noqa: E402
from validate_content import validate  # noqa: E402


README = """# A. Theatre Square

**Submission:** https://codeforces.com/contest/1/problem/A

**Limits:** 1 second / 256 megabytes

**Rating:** 1000

**Tags:** math

## Problem Statement

Cover the square.
"""


class CodeforcesContentToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.problem = (
            self.root
            / "0001-0100"
            / "1 - Round #1"
            / "A - Theatre Square"
        )
        self.problem.mkdir(parents=True)
        (self.problem / "README.md").write_text(README, encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_validator_discovers_contest_problem_layout(self) -> None:
        contests, errors = validate(self.root)

        self.assertEqual([], errors)
        self.assertEqual([1], [contest.contest_id for contest in contests])
        self.assertEqual(["1-A"], [problem.key for problem in contests[0].problems])

    def test_builder_packages_arbitrary_approaches_and_images(self) -> None:
        image = self.problem / "images" / "sample.png"
        image.parent.mkdir()
        image.write_bytes(b"\x89PNG\r\n\x1a\n")
        (self.problem / "README.md").write_text(
            README + "\n![Grid](images/sample.png)\n",
            encoding="utf-8",
        )
        for number in (1, 12):
            approach = self.problem / f"Approach {number}"
            approach.mkdir()
            (approach / "main.cpp").write_text(
                f"int main() {{ return {number}; }}",
                encoding="utf-8",
            )
        output = self.root / "dist"

        build(
            self.root,
            output,
            "fixed-version",
            "2026-01-01T00:00:00Z",
        )

        with zipfile.ZipFile(output / "content-package.zip") as archive:
            names = archive.namelist()
            self.assertIn("codeforces_seed/manifest.json", names)
            self.assertIn("codeforces_seed/contests/0001.json", names)
            contest = json.loads(
                archive.read("codeforces_seed/contests/0001.json")
            )
            problem = contest["problems"][0]
            self.assertEqual(["math"], problem["tags"])
            self.assertEqual(
                [1, 12],
                [approach["number"] for approach in problem["approaches"]],
            )
            self.assertTrue(
                any(block["type"] == "image" for block in problem["contentBlocks"])
            )

    def test_package_is_deterministic(self) -> None:
        first = self.root / "first"
        second = self.root / "second"

        build(
            self.root,
            first,
            "fixed-version",
            "2026-01-01T00:00:00Z",
        )
        build(
            self.root,
            second,
            "fixed-version",
            "2026-01-01T00:00:00Z",
        )

        self.assertEqual(
            sha256_file(first / "content-package.zip"),
            sha256_file(second / "content-package.zip"),
        )

    def test_scaffolder_supports_any_problem_count(self) -> None:
        contest = create_contest(
            self.root,
            2050,
            "Round 2050",
            ["A:First", "B:Second", "F2:Final"],
            approach_count=3,
        )

        self.assertEqual("2001-2100", contest.parent.name)
        self.assertTrue((contest / "F2 - Final" / "README.md").is_file())
        self.assertTrue(
            (contest / "F2 - Final" / "Approach 3" / "main.cpp").is_file()
        )
        self.assertTrue((contest / "F2 - Final" / "images" / ".gitkeep").is_file())

    def test_builder_can_bundle_one_contest_for_the_app_seed(self) -> None:
        second = (
            self.root
            / "0101-0200"
            / "101 - Round #101"
            / "A - Another"
        )
        second.mkdir(parents=True)
        (second / "README.md").write_text(
            README.replace("/contest/1/problem/A", "/contest/101/problem/A"),
            encoding="utf-8",
        )
        output = self.root / "single"

        build(
            self.root,
            output,
            "fixed-version",
            "2026-01-01T00:00:00Z",
            contest_id=1,
        )

        with zipfile.ZipFile(output / "content-package.zip") as archive:
            manifest = json.loads(
                archive.read("codeforces_seed/manifest.json")
            )
            self.assertEqual(1, manifest["contestCount"])
            self.assertEqual(
                "2026-01-01T00:00:00Z",
                manifest["generatedAt"],
            )
            self.assertEqual(
                ["codeforces_seed/contests/0001.json"],
                [
                    name
                    for name in archive.namelist()
                    if name.startswith("codeforces_seed/contests/")
                ],
            )


if __name__ == "__main__":
    unittest.main()
