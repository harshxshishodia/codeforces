# B. Platforms

**Submission:** https://codeforces.com/contest/18/problem/B

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

In one one-dimensional world there are n platforms. Platform with index k (platforms are numbered from 1) is a segment with coordinates [( k ΓÇë-ΓÇë1) m ,ΓÇë( k ΓÇë-ΓÇë1) m ΓÇë+ΓÇë l ] , and l ΓÇë<ΓÇë m . Grasshopper Bob starts to jump along the platforms from point 0 , with each jump he moves exactly d units right. Find out the coordinate of the point, where Bob will fall down. The grasshopper falls down, if he finds himself not on the platform, but if he finds himself on the edge of the platform, he doesn't fall down.

## Input

The first input line contains 4 integer numbers n , d , m , l ( 1ΓÇëΓëñΓÇë n ,ΓÇë d ,ΓÇë m ,ΓÇë l ΓÇëΓëñΓÇë10 6 ,ΓÇë l ΓÇë<ΓÇë m ) ΓÇö respectively: amount of platforms, length of the grasshopper Bob's jump, and numbers m and l needed to find coordinates of the k -th platform: [( k ΓÇë-ΓÇë1) m ,ΓÇë( k ΓÇë-ΓÇë1) m ΓÇë+ΓÇë l ] .

## Output

Output the coordinates of the point, where the grosshopper will fall down. Don't forget that if Bob finds himself on the platform edge, he doesn't fall down.

## Examples

Example 1:
```
2 2 5 3
```
```
4
```
