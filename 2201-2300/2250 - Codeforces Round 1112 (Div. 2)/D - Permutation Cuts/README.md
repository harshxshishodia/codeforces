# D. Permutation Cuts

**Submission:** https://codeforces.com/contest/2250/problem/D

**Limits:** 4 seconds / 256 megabytes

**Tags:** combinatorics, implementation, math

## Problem Statement

For every cut in a permutation, take the maximum value on each side and record
the smaller of those two maxima. Given the resulting array, count how many
permutations of length `n` produce it.

## Input

The first line contains `t` test cases. Each case gives `n` and an array of
length `n-1`. The sum of `n` is at most `10^6`.

## Output

Print the number of valid permutations modulo `998244353`.
