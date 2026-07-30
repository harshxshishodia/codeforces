# C. Sequence of points

**Submission:** https://codeforces.com/contest/24/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

You are given the following points with integer coordinates on the plane: M 0 ,ΓÇë A 0 ,ΓÇë A 1 ,ΓÇë...,ΓÇë A n ΓÇë-ΓÇë1 , where n is odd number. Now we define the following infinite sequence of points M i : M i is symmetric to M i ΓÇë-ΓÇë1 according (for every natural number i ). Here point B is symmetric to A according M , if M is the center of the line segment AB . Given index j find the point M j .

## Input

On the first line you will be given an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ), which will be odd, and j ( 1ΓÇëΓëñΓÇë j ΓÇëΓëñΓÇë10 18 ), where j is the index of the desired point. The next line contains two space separated integers, the coordinates of M 0 . After that n lines follow, where the i -th line contain the space separated integer coordinates of the point A i ΓÇë-ΓÇë1 . The absolute values of all input coordinates will not be greater then 1000 .

## Output

On a single line output the coordinates of M j , space separated.

## Examples

Example 1:
```
3 4
0 0
1 1
2 3
-5 3
```
```
14 0
```
