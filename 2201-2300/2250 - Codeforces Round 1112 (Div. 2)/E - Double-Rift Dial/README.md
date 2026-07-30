# E. Double-Rift Dial

**Submission:** https://codeforces.com/contest/2250/problem/E

**Limits:** 2 seconds / 256 megabytes

**Tags:** data structures, implementation

## Problem Statement

A permutation is placed around a circle. Starting from any position, read one
full rotation. A start is good when the set of values in every non-empty prefix
can be split into at most two maximal intervals of consecutive integers. Count
the good starting positions.

## Input

The first line contains `t` test cases. Each case gives `n` and a permutation
of `1..n`. The sum of `n` is at most `2 * 10^5`.

## Output

Print the number of good starting positions for each test case.
