# C. Rank Subsequence

**Submission:** https://codeforces.com/contest/2250/problem/C

**Limits:** 2 seconds / 256 megabytes

**Tags:** brute force, greedy, implementation

## Problem Statement

Delete any elements from a line to form a subsequence. An element kept at
position `j` in a subsequence of length `m` is valid only when its left rank
`j` avoids one forbidden interval and its right rank `m-j+1` avoids another.
Find the maximum possible length of a subsequence in which every element is
valid.

## Input

The first line contains `t` test cases. Each case gives `n`, followed by `n`
rows containing the four interval endpoints. The sum of `n` is at most `5000`.

## Output

Print the maximum valid subsequence length for each test case.
