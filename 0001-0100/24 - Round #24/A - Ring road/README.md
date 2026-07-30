# A. Ring road

**Submission:** https://codeforces.com/contest/24/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Nowadays the one-way traffic is introduced all over the world in order to improve driving safety and reduce traffic jams. The government of Berland decided to keep up with new trends. Formerly all n cities of Berland were connected by n two-way roads in the ring, i. e. each city was connected directly to exactly two other cities, and from each city it was possible to get to any other city. Government of Berland introduced one-way traffic on all n roads, but it soon became clear that it's impossible to get from some of the cities to some others. Now for each road is known in which direction the traffic is directed at it, and the cost of redirecting the traffic. What is the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other?

## Input

The first line contains integer n ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö amount of cities (and roads) in Berland. Next n lines contain description of roads. Each road is described by three integers a i , b i , c i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë a i ΓÇëΓëáΓÇë b i ,ΓÇë1ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë100 ) ΓÇö road is directed from city a i to city b i , redirecting the traffic costs c i .

## Output

Output single integer ΓÇö the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other.

## Examples

Example 1:
```
3
1 3 1
1 2 1
3 2 1
```
```
1
```
