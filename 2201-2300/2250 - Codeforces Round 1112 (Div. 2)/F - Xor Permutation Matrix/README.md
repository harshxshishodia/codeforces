# F. Xor Permutation Matrix

**Submission:** https://codeforces.com/contest/2250/problem/F

**Limits:** 2 seconds / 512 megabytes

**Tags:** bitmasks, constructive algorithms, math

## Problem Statement

Construct an `n x n` matrix whose rows and columns are all permutations of
`0..n-1`. Every adjacent `2 x 2` submatrix must have XOR equal to `x`.
Determine when the construction is impossible.

## Input

The first line contains `t` test cases. Each case contains `n` and `x`, with
`2 <= n <= 2500` and `0 <= x < n`. The sum of `n` is at most `2500`.

## Output

Print `-1` if no matrix exists; otherwise print any valid matrix.
