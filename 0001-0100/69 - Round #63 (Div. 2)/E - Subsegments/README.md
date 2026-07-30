# E. Subsegments

**Submission:** https://codeforces.com/contest/69/problem/E

**Limits:** 1 second / 256 megabytes

## Problem Statement

Programmer Sasha has recently begun to study data structures. His coach Stas told him to solve the problem of finding a minimum on the segment of the array in , which Sasha coped with. For Sasha not to think that he had learned all, Stas gave him a new task. For each segment of the fixed length Sasha must find the maximum element of those that occur on the given segment exactly once. Help Sasha solve this problem.

## Input

The first line contains two positive integers n and k ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ,ΓÇë1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë n ) ΓÇö the number of array elements and the length of the segment. 

Then follow n lines: the i -th one contains a single number a i ( ΓÇë-ΓÇë10 9 ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ).

## Output

Print n ΓÇô k ΓÇë+ΓÇë1 numbers, one per line: on the i -th line print of the maximum number of those numbers from the subarray a i a i ΓÇë+ΓÇë1 ΓÇª a i ΓÇë+ΓÇë k ΓÇë-ΓÇë1 that occur in this subarray exactly 1 time. If there are no such numbers in this subarray, print " Nothing ".

## Examples

Example 1:
```
5 3
1
2
2
3
3
```
```
1
3
2
```
