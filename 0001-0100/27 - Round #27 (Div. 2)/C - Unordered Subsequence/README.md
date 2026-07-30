# C. Unordered Subsequence

**Submission:** https://codeforces.com/contest/27/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

The sequence is called ordered if it is non-decreasing or non-increasing. For example, sequnces [3, 1, 1, 0] and [1, 2, 3, 100] are ordered, but the sequence [1, 3, 3, 1] is not. You are given a sequence of numbers. You are to find it's shortest subsequence which is not ordered.

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

## Input

The first line of the input contains one integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ). The second line contains n space-separated integers ΓÇö the given sequence. All numbers in this sequence do not exceed 10 6 by absolute value.

## Output

If the given sequence does not contain any unordered subsequences, output 0 . Otherwise, output the length k of the shortest such subsequence. Then output k integers from the range [1.. n ] ΓÇö indexes of the elements of this subsequence. If there are several solutions, output any of them.

## Examples

Example 1:
```
5
67 499 600 42 23
```
```
3
1 3 5
```
