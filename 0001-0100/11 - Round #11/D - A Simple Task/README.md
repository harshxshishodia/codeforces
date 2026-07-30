# D. A Simple Task

**Submission:** https://codeforces.com/contest/11/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Given a simple graph, output the number of simple cycles in it. A simple cycle is a cycle with no repeated vertices or edges.

## Input

The first line of input contains two integers n and m ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë19 , 0ΓÇëΓëñΓÇë m ) ΓÇô respectively the number of vertices and edges of the graph. Each of the subsequent m lines contains two integers a and b , ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ΓÇëΓëñΓÇë n , a ΓÇëΓëáΓÇë b ) indicating that vertices a and b are connected by an undirected edge. There is no more than one edge connecting any pair of vertices.

## Output

Output the number of cycles in the given graph.

## Examples

Example 1:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
```
7
```

## Note

The example graph is a clique and contains four cycles of length 3 and three cycles of length 4.
