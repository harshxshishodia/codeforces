# B. String Construction

**Submission:** https://codeforces.com/contest/2250/problem/B

**Limits:** 1 second / 256 megabytes

**Tags:** constructive algorithms

## Problem Statement

Construct a binary string of length `n` whose counts of zeroes and ones differ
by at most one, while exactly `k` adjacent pairs contain equal characters.
Report when no such string can be built.

## Input

The first line contains `t` test cases. Each case contains `n` and `k`, with
`2 <= n <= 2 * 10^5` and `0 <= k < n`. The total `n` is at most `2 * 10^5`.

## Output

Print any valid string for each test case, or `-1` if construction is
impossible.
