# D. King's Problem?

**Submission:** https://codeforces.com/contest/30/problem/D

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

Every true king during his life must conquer the world, hold the Codeforces world finals, win pink panda in the shooting gallery and travel all over his kingdom.

King Copa has already done the first three things. Now he just needs to travel all over the kingdom. The kingdom is an infinite plane with Cartesian coordinate system on it. Every city is a point on this plane. There are n cities in the kingdom at points with coordinates ( x 1 ,ΓÇë0),ΓÇë( x 2 ,ΓÇë0),ΓÇë...,ΓÇë( x n ,ΓÇë0) , and there is one city at point ( x n ΓÇë+ΓÇë1 ,ΓÇë y n ΓÇë+ΓÇë1 ) . 

King starts his journey in the city number k . Your task is to find such route for the king, which visits all cities (in any order) and has minimum possible length. It is allowed to visit a city twice. The king can end his journey in any city. Between any pair of cities there is a direct road with length equal to the distance between the corresponding points. No two cities may be located at the same point.

## Input

The first line contains two integers n and k ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ,ΓÇë1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë n ΓÇë+ΓÇë1 ) ΓÇö amount of cities and index of the starting city. The second line contains n ΓÇë+ΓÇë1 numbers x i . The third line contains y n ΓÇë+ΓÇë1 . All coordinates are integers and do not exceed 10 6 by absolute value. No two cities coincide.

## Output

Output the minimum possible length of the journey. Your answer must have relative or absolute error less than 10 ΓÇë-ΓÇë6 .

## Examples

Example 1:
```
3 1
0 1 2 1
1
```
```
3.41421356237309490000
```
