# C. Parquet

**Submission:** https://codeforces.com/contest/26/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Once Bob decided to lay a parquet floor in his living room. The living room is of size n ΓÇë├ùΓÇë m metres. Bob had planks of three types: a planks 1ΓÇë├ùΓÇë2 meters, b planks 2ΓÇë├ùΓÇë1 meters, and c planks 2ΓÇë├ùΓÇë2 meters. Help Bob find out, if it is possible to parquet the living room with such a set of planks, and if it is possible, find one of the possible ways to do so. Bob doesn't have to use all the planks.

## Input

The first input line contains 5 space-separated integer numbers n , m , a , b , c ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë100,ΓÇë0ΓÇëΓëñΓÇë a ,ΓÇë b ,ΓÇë c ΓÇëΓëñΓÇë10 4 ), n and m ΓÇö the living room dimensions, a , b and c ΓÇö amount of planks 1ΓÇë├ùΓÇë2 , 2ΓÇë├ùΓÇë1 ╨╕ 2ΓÇë├ùΓÇë2 respectively. It's not allowed to turn the planks.

## Output

If it is not possible to parquet the room with such a set of planks, output IMPOSSIBLE . Otherwise output one of the possible ways to parquet the room ΓÇö output n lines with m lower-case Latin letters each. Two squares with common sides should contain the same letters, if they belong to one and the same plank, and different letters otherwise. Different planks can be marked with one and the same letter (see examples). If the answer is not unique, output any.

## Examples

Example 1:
```
2 6 2 2 1
```
```
aabcca
aabdda
```
