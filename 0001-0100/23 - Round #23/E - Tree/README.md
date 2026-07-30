# E. Tree

**Submission:** https://codeforces.com/contest/23/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Recently Bob invented a new game with a tree (we should remind you, that a tree is a connected graph without cycles): he deletes any (possibly, zero) amount of edges of the tree, and counts the product of sizes of the connected components left after the deletion. Your task is to find out the maximum number that Bob can get in his new game for a given tree.

## Input

The first input line contains integer number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë700 ) ΓÇö amount of vertices in the tree. The following n ΓÇë-ΓÇë1 lines contain the description of the edges. Each line contains the pair of vertices' indexes, joined by an edge, a i , b i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ). It's guaranteed that the graph described in the input is a tree.

## Output

Output the only number ΓÇö the maximum product of sizes of the connected components, that Bob can get after deleting some of the tree's edges.

## Examples

Example 1:
```
5
1 2
2 3
3 4
4 5
```
```
6
```
