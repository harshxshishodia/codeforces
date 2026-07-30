# E. Camels

**Submission:** https://codeforces.com/contest/14/problem/E

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

Bob likes to draw camels: with a single hump, two humps, three humps, etc. He draws a camel by connecting points on a coordinate plane. Now he's drawing camels with t humps, representing them as polylines in the plane. Each polyline consists of n vertices with coordinates ( x 1 ,ΓÇë y 1 ) , ( x 2 ,ΓÇë y 2 ) , ..., ( x n ,ΓÇë y n ) . The first vertex has a coordinate x 1 ΓÇë=ΓÇë1 , the second ΓÇö x 2 ΓÇë=ΓÇë2 , etc. Coordinates y i might be any, but should satisfy the following conditions:

 
- there should be t humps precisely, i.e. such indexes j ( 2ΓÇëΓëñΓÇë j ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1 ), so that y j ΓÇë-ΓÇë1 ΓÇë<ΓÇë y j ΓÇë>ΓÇë y j ΓÇë+ΓÇë1 , 
- there should be precisely t ΓÇë-ΓÇë1 such indexes j ( 2ΓÇëΓëñΓÇë j ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1 ), so that y j ΓÇë-ΓÇë1 ΓÇë>ΓÇë y j ΓÇë<ΓÇë y j ΓÇë+ΓÇë1 , 
- no segment of a polyline should be parallel to the Ox -axis, 
- all y i are integers between 1 and 4. 

For a series of his drawings of camels with t humps Bob wants to buy a notebook, but he doesn't know how many pages he will need. Output the amount of different polylines that can be drawn to represent camels with t humps for a given number n .

## Input

The first line contains a pair of integers n and t ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë20 , 1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë10 ).

## Output

Output the required amount of camels with t humps.

## Examples

Example 1:
```
6 1
```
```
6
```

## Note

In the first sample test sequences of y -coordinates for six camels are: 123421, 123431, 123432, 124321, 134321 ╨╕ 234321 (each digit corresponds to one value of y i ).
