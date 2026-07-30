# C. Roads in Berland

**Submission:** https://codeforces.com/contest/25/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There are n cities numbered from 1 to n in Berland. Some of them are connected by two-way roads. Each road has its own length ΓÇö an integer number from 1 to 1000. It is known that from each city it is possible to get to any other city by existing roads. Also for each pair of cities it is known the shortest distance between them. Berland Government plans to build k new roads. For each of the planned road it is known its length, and what cities it will connect. To control the correctness of the construction of new roads, after the opening of another road Berland government wants to check the sum of the shortest distances between all pairs of cities. Help them ΓÇö for a given matrix of shortest distances on the old roads and plans of all new roads, find out how the sum of the shortest distances between all pairs of cities changes after construction of each road.

## Input

The first line contains integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë300 ) ΓÇö amount of cities in Berland. Then there follow n lines with n integer numbers each ΓÇö the matrix of shortest distances. j -th integer in the i -th row ΓÇö d i ,ΓÇë j , the shortest distance between cities i and j . It is guaranteed that d i ,ΓÇë i ΓÇë=ΓÇë0,ΓÇë d i ,ΓÇë j ΓÇë=ΓÇë d j ,ΓÇë i , and a given matrix is a matrix of shortest distances for some set of two-way roads with integer lengths from 1 to 1000, such that from each city it is possible to get to any other city using these roads.

Next line contains integer k ( 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë300 ) ΓÇö amount of planned roads. Following k lines contain the description of the planned roads. Each road is described by three space-separated integers a i , b i , c i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë a i ΓÇëΓëáΓÇë b i ,ΓÇë1ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë1000 ) ΓÇö a i and b i ΓÇö pair of cities, which the road connects, c i ΓÇö the length of the road. It can be several roads between a pair of cities, but no road connects the city with itself.

## Output

Output k space-separated integers q i ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë k ). q i should be equal to the sum of shortest distances between all pairs of cities after the construction of roads with indexes from 1 to i . Roads are numbered from 1 in the input order. Each pair of cities should be taken into account in the sum exactly once, i. e. we count unordered pairs.

## Examples

Example 1:
```
2
0 5
5 0
1
1 2 3
```
```
3
```
