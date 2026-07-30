# D. Chocolate

**Submission:** https://codeforces.com/contest/31/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Bob has a rectangular chocolate bar of the size W ΓÇë├ùΓÇë H . He introduced a cartesian coordinate system so that the point (0,ΓÇë0) corresponds to the lower-left corner of the bar, and the point ( W ,ΓÇë H ) corresponds to the upper-right corner. Bob decided to split the bar into pieces by breaking it. Each break is a segment parallel to one of the coordinate axes, which connects the edges of the bar. More formally, each break goes along the line x ΓÇë=ΓÇë x c or y ΓÇë=ΓÇë y c , where x c and y c are integers. It should divide one part of the bar into two non-empty parts. After Bob breaks some part into two parts, he breaks the resulting parts separately and independently from each other . Also he doesn't move the parts of the bar. Bob made n breaks and wrote them down in his notebook in arbitrary order. At the end he got n ΓÇë+ΓÇë1 parts. Now he wants to calculate their areas. Bob is lazy, so he asks you to do this task.

## Input

The first line contains 3 integers W , H and n ( 1ΓÇëΓëñΓÇë W ,ΓÇë H ,ΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö width of the bar, height of the bar and amount of breaks. Each of the following n lines contains four integers x i ,ΓÇë1 ,ΓÇë y i ,ΓÇë1 ,ΓÇë x i ,ΓÇë2 ,ΓÇë y i ,ΓÇë2 ΓÇö coordinates of the endpoints of the i -th break ( 0ΓÇëΓëñΓÇë x i ,ΓÇë1 ΓÇëΓëñΓÇë x i ,ΓÇë2 ΓÇëΓëñΓÇë W ,ΓÇë0ΓÇëΓëñΓÇë y i ,ΓÇë1 ΓÇëΓëñΓÇë y i ,ΓÇë2 ΓÇëΓëñΓÇë H , or x i ,ΓÇë1 ΓÇë=ΓÇë x i ,ΓÇë2 , or y i ,ΓÇë1 ΓÇë=ΓÇë y i ,ΓÇë2 ). Breaks are given in arbitrary order.

It is guaranteed that the set of breaks is correct, i.e. there is some order of the given breaks that each next break divides exactly one part of the bar into two non-empty parts.

## Output

Output n ΓÇë+ΓÇë1 numbers ΓÇö areas of the resulting parts in the increasing order.

## Examples

Example 1:
```
2 2 2
1 0 1 2
0 1 1 1
```
```
1 1 2
```
