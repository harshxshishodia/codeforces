# A. Threshold Movement

**Submission:** https://codeforces.com/contest/2250/problem/A

**Limits:** 1 second / 256 megabytes

**Tags:** brute force, implementation, math

## Problem Statement

Choose an integer threshold `k` for a line of weighted elements. Every element
lighter than `k` moves one position left, every heavier element moves one
position right, and the process fails if any weight equals `k`. Determine
whether some integer threshold leaves exactly one element in every original
position.

## Input

The first line contains `t` test cases. Each case contains `n` (`1 <= n <= 100`)
and `n` weights, each between `1` and `10^9`.

## Output

Print `YES` when a perfect threshold exists; otherwise print `NO`.
