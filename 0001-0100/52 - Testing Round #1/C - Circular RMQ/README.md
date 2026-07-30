# C. Circular RMQ

**Submission:** https://codeforces.com/contest/52/problem/C

**Limits:** 1.5 seconds / 256 megabytes

## Problem Statement

You are given circular array a 0 ,ΓÇë a 1 ,ΓÇë...,ΓÇë a n ΓÇë-ΓÇë1 . There are two types of operations with it: 

 
- inc ( lf ,ΓÇë rg ,ΓÇë v ) ΓÇö this operation increases each element on the segment [ lf ,ΓÇë rg ] (inclusively) by v ; 
- rmq ( lf ,ΓÇë rg ) ΓÇö this operation returns minimal value on the segment [ lf ,ΓÇë rg ] (inclusively). 

Assume segments to be circular, so if n ΓÇë=ΓÇë5 and lf ΓÇë=ΓÇë3,ΓÇë rg ΓÇë=ΓÇë1 , it means the index sequence: 3,ΓÇë4,ΓÇë0,ΓÇë1 .

Write program to process given sequence of operations.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë200000 ). The next line contains initial state of the array: a 0 ,ΓÇë a 1 ,ΓÇë...,ΓÇë a n ΓÇë-ΓÇë1 ( ΓÇë-ΓÇë10 6 ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 6 ), a i are integer. The third line contains integer m ( 0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë200000 ), m ΓÇö the number of operartons. Next m lines contain one operation each. If line contains two integer lf ,ΓÇë rg ( 0ΓÇëΓëñΓÇë lf ,ΓÇë rg ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1 ) it means rmq operation, it contains three integers lf ,ΓÇë rg ,ΓÇë v ( 0ΓÇëΓëñΓÇë lf ,ΓÇë rg ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1;ΓÇë-ΓÇë10 6 ΓÇëΓëñΓÇë v ΓÇëΓëñΓÇë10 6 ) ΓÇö inc operation.

## Output

For each rmq operation write result for it. Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d ).

## Examples

Example 1:
```
4
1 2 3 4
4
3 0
3 0 -1
0 1
2 1
```
```
1
0
0
```
