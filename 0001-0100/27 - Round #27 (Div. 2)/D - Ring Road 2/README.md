# D. Ring Road 2

**Submission:** https://codeforces.com/contest/27/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

It is well known that Berland has n cities, which form the Silver ring ΓÇö cities i and i ΓÇë+ΓÇë1 ( 1ΓÇëΓëñΓÇë i ΓÇë<ΓÇë n ) are connected by a road, as well as the cities n and 1 . The goverment have decided to build m new roads. The list of the roads to build was prepared. Each road will connect two cities. Each road should be a curve which lies inside or outside the ring. New roads will have no common points with the ring (except the endpoints of the road).

Now the designers of the constructing plan wonder if it is possible to build the roads in such a way that no two roads intersect (note that the roads may intersect at their endpoints). If it is possible to do, which roads should be inside the ring, and which should be outside?

## Input

The first line contains two integers n and m ( 4ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100,ΓÇë1ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë100 ). Each of the following m lines contains two integers a i and b i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë a i ΓÇëΓëáΓÇë b i ). No two cities will be connected by more than one road in the list. The list will not contain the roads which exist in the Silver ring.

## Output

If it is impossible to build the roads in such a way that no two roads intersect, output Impossible . Otherwise print m characters. i -th character should be i , if the road should be inside the ring, and o if the road should be outside the ring. If there are several solutions, output any of them.

## Examples

Example 1:
```
4 2
1 3
2 4
```
```
io
```
