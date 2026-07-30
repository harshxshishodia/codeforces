# C. Dijkstra?

**Submission:** https://codeforces.com/contest/20/problem/C

**Limits:** 1 second / 64 megabytes

## Problem Statement

You are given a weighted undirected graph. The vertices are enumerated from 1 to n . Your task is to find the shortest path between the vertex 1 and the vertex n .

## Input

The first line contains two integers n and m ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ,ΓÇë0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10 5 ), where n is the number of vertices and m is the number of edges. Following m lines contain one edge each in form a i , b i and w i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë w i ΓÇëΓëñΓÇë10 6 ), where a i ,ΓÇë b i are edge endpoints and w i is the length of the edge.

It is possible that the graph has loops and multiple edges between pair of vertices.

## Output

Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many solutions, print any of them.

## Examples

Example 1:
```
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1
```
```
1 4 3 5
```
