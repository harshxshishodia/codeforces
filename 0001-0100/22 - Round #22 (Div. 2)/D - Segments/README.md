# D. Segments

**Submission:** https://codeforces.com/contest/22/problem/D

**Limits:** 1 second / 256 megabytes

## Problem Statement

You are given n segments on the Ox-axis. You can drive a nail in any integer point on the Ox-axis line nail so, that all segments containing this point, are considered nailed down. If the nail passes through endpoint of some segment, this segment is considered to be nailed too. What is the smallest number of nails needed to nail all the segments down?

## Input

The first line of the input contains single integer number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) ΓÇö amount of segments. Following n lines contain descriptions of the segments. Each description is a pair of integer numbers ΓÇö endpoints coordinates. All the coordinates don't exceed 10000 by absolute value. Segments can degenarate to points.

## Output

The first line should contain one integer number ΓÇö the smallest number of nails needed to nail all the segments down. The second line should contain coordinates of driven nails separated by space in any order. If the answer is not unique, output any.

## Examples

Example 1:
```
2
0 2
2 5
```
```
1
2
```
