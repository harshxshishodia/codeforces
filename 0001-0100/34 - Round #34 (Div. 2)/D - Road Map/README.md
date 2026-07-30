# D. Road Map

**Submission:** https://codeforces.com/contest/34/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There are n cities in Berland. Each city has its index ΓÇö an integer number from 1 to n . The capital has index r 1 . All the roads in Berland are two-way. The road system is such that there is exactly one path from the capital to each city, i.e. the road map looks like a tree. In Berland's chronicles the road map is kept in the following way: for each city i , different from the capital, there is kept number p i ΓÇö index of the last city on the way from the capital to i .

Once the king of Berland Berl XXXIV decided to move the capital from city r 1 to city r 2 . Naturally, after this the old representation of the road map in Berland's chronicles became incorrect. Please, help the king find out a new representation of the road map in the way described above.

## Input

The first line contains three space-separated integers n , r 1 , r 2 ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë5┬╖10 4 ,ΓÇë1ΓÇëΓëñΓÇë r 1 ΓÇëΓëáΓÇë r 2 ΓÇëΓëñΓÇë n ) ΓÇö amount of cities in Berland, index of the old capital and index of the new one, correspondingly.

The following line contains n ΓÇë-ΓÇë1 space-separated integers ΓÇö the old representation of the road map. For each city, apart from r 1 , there is given integer p i ΓÇö index of the last city on the way from the capital to city i . All the cities are described in order of increasing indexes.

## Output

Output n ΓÇë-ΓÇë1 numbers ΓÇö new representation of the road map in the same format.

## Examples

Example 1:
```
3 2 3
2 2
```
```
2 3
```
