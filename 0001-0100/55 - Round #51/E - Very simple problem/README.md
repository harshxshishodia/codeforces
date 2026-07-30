# E. Very simple problem

**Submission:** https://codeforces.com/contest/55/problem/E

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

You are given a convex polygon. Count, please, the number of triangles that contain a given point in the plane and their vertices are the vertices of the polygon. It is guaranteed, that the point doesn't lie on the sides and the diagonals of the polygon.

## Input

The first line contains integer n ΓÇö the number of vertices of the polygon ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100000 ). The polygon description is following: n lines containing coordinates of the vertices in clockwise order (integer x and y not greater than 10 9 by absolute value). It is guaranteed that the given polygon is nondegenerate and convex (no three points lie on the same line).

The next line contains integer t ( 1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë20 ) ΓÇö the number of points which you should count the answer for. It is followed by t lines with coordinates of the points (integer x and y not greater than 10 9 by absolute value).

## Output

The output should contain t integer numbers, each on a separate line, where i -th number is the answer for the i -th point.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d ).

## Examples

Example 1:
```
4
5 0
0 0
0 5
5 5
1
1 3
```
```
2
```
