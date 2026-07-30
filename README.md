# Codeforces Contest Content

This repository is the source of the Android app's Codeforces platform. Content is
organized by contest, while each problem can contain any number of approaches and
programming languages.

```text
0001-0100/
  1 - Round #1/
    A - Theatre Square/
      README.md
      images/
      Approach 1/
        main.cpp
      Approach 2/
        main.py
```

Contest range folders are created in blocks of 100. Contest folders use
`<contest id> - <contest name>`. Problem folders use
`<problem index> - <problem name>` and may use indices such as `A`, `F`, or `F2`.

Each problem `README.md` uses this metadata before the statement:

```markdown
# A. Problem name

**Submission:** https://codeforces.com/contest/1/problem/A

**Limits:** 1 second / 256 megabytes

**Rating:** 1000

**Tags:** math, implementation
```

`Tags` should use Codeforces topic names. Local Markdown or HTML image references
are copied into the mobile package. Empty `images/` folders are allowed.

Create a contest with any number of problems:

```powershell
python tools/create_contest.py --contest 2000 --name "Round #2000" `
  --problem "A:First Problem" --problem "B:Second Problem" --approaches 2
```

Validate, test, and build:

```powershell
python tools/validate_content.py --content-root .
python -m unittest discover -s tools/tests -v
python tools/build_mobile_package.py --content-root .
```

Every push to `main` validates and publishes the verified snapshot to the
`mobile-content` branch. The Android app reads that branch from
`github.com/harshxshishodia/codeforces`.
