# D. Geometrical problem

**Submission:** https://codeforces.com/contest/51/problem/D

**Limits:** 1 second / 256 megabytes

## Problem Statement

Polycarp loves geometric progressions ΓÇö he collects them. However, as such progressions occur very rarely, he also loves the sequences of numbers where it is enough to delete a single element to get a geometric progression.

In this task we shall define geometric progressions as finite sequences of numbers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a k , where a i ΓÇë=ΓÇë c ┬╖ b i ΓÇë-ΓÇë1 for some real numbers c and b . For example, the sequences [2, -4, 8], [0, 0, 0, 0], [199] are geometric progressions and [0, 1, 2, 3] is not.

Recently Polycarp has found a sequence and he can't classify it. Help him to do it. Determine whether it is a geometric progression. If it is not, check if it can become a geometric progression if an element is deleted from it.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö the number of elements in the given sequence. The second line contains the given sequence. The numbers are space-separated. All the elements of the given sequence are integers and their absolute value does not exceed 10 4 .

## Output

Print 0 , if the given sequence is a geometric progression. Otherwise, check if it is possible to make the sequence a geometric progression by deleting a single element. If it is possible, print 1 . If it is impossible, print 2 .

## Examples

Example 1:
```
4
3 6 12 24
```
```
0
```
