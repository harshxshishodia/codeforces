# B. Restoration of the Permutation

**Submission:** https://codeforces.com/contest/67/problem/B

**Limits:** 1 second / 256 megabytes

## Problem Statement

Let A ΓÇë=ΓÇë{ a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n } be any permutation of the first n natural numbers {1,ΓÇë2,ΓÇë...,ΓÇë n } . You are given a positive integer k and another sequence B ΓÇë=ΓÇë{ b 1 ,ΓÇë b 2 ,ΓÇë...,ΓÇë b n } , where b i is the number of elements a j in A to the left of the element a t ΓÇë=ΓÇë i such that a j ΓÇëΓëÑΓÇë( i ΓÇë+ΓÇë k ) .

For example, if n ΓÇë=ΓÇë5 , a possible A is {5,ΓÇë1,ΓÇë4,ΓÇë2,ΓÇë3} . For k ΓÇë=ΓÇë2 , B is given by {1,ΓÇë2,ΓÇë1,ΓÇë0,ΓÇë0} . But if k ΓÇë=ΓÇë3 , then B ΓÇë=ΓÇë{1,ΓÇë1,ΓÇë0,ΓÇë0,ΓÇë0} .

For two sequences X ΓÇë=ΓÇë{ x 1 ,ΓÇë x 2 ,ΓÇë...,ΓÇë x n } and Y ΓÇë=ΓÇë{ y 1 ,ΓÇë y 2 ,ΓÇë...,ΓÇë y n } , let i -th elements be the first elements such that x i ΓÇëΓëáΓÇë y i . If x i ΓÇë<ΓÇë y i , then X is lexicographically smaller than Y , while if x i ΓÇë>ΓÇë y i , then X is lexicographically greater than Y .

Given n , k and B , you need to determine the lexicographically smallest A .

## Input

The first line contains two space separated integers n and k ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 , 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë n ). On the second line are n integers specifying the values of B ΓÇë=ΓÇë{ b 1 ,ΓÇë b 2 ,ΓÇë...,ΓÇë b n } .

## Output

Print on a single line n integers of A ΓÇë=ΓÇë{ a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n } such that A is lexicographically minimal. It is guaranteed that the solution exists.

## Examples

Example 1:
```
5 2
1 2 1 0 0
```
```
4 1 5 2 3
```
