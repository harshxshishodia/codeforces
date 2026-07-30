# D. Points

**Submission:** https://codeforces.com/contest/19/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Pete and Bob invented a new interesting game. Bob takes a sheet of paper and locates a Cartesian coordinate system on it as follows: point (0,ΓÇë0) is located in the bottom-left corner, Ox axis is directed right, Oy axis is directed up. Pete gives Bob requests of three types: 

 
- add x y ΓÇö on the sheet of paper Bob marks a point with coordinates ( x ,ΓÇë y ) . For each request of this type it's guaranteed that point ( x ,ΓÇë y ) is not yet marked on Bob's sheet at the time of the request. 
- remove x y ΓÇö on the sheet of paper Bob erases the previously marked point with coordinates ( x ,ΓÇë y ) . For each request of this type it's guaranteed that point ( x ,ΓÇë y ) is already marked on Bob's sheet at the time of the request. 
- find x y ΓÇö on the sheet of paper Bob finds all the marked points, lying strictly above and strictly to the right of point ( x ,ΓÇë y ) . Among these points Bob chooses the leftmost one, if it is not unique, he chooses the bottommost one, and gives its coordinates to Pete. 

Bob managed to answer the requests, when they were 10, 100 or 1000, but when their amount grew up to 2┬╖10 5 , Bob failed to cope. Now he needs a program that will answer all Pete's requests. Help Bob, please!

## Input

The first input line contains number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë2┬╖10 5 ) ΓÇö amount of requests. Then there follow n lines ΓÇö descriptions of the requests. add x y describes the request to add a point, remove x y ΓÇö the request to erase a point, find x y ΓÇö the request to find the bottom-left point. All the coordinates in the input file are non-negative and don't exceed 10 9 .

## Output

For each request of type find x y output in a separate line the answer to it ΓÇö coordinates of the bottommost among the leftmost marked points, lying strictly above and to the right of point ( x ,ΓÇë y ) . If there are no points strictly above and to the right of point ( x ,ΓÇë y ) , output -1 .

## Examples

Example 1:
```
7
add 1 1
add 3 4
find 0 0
remove 1 1
find 0 0
add 1 1
find 0 0
```
```
1 1
3 4
1 1
```
