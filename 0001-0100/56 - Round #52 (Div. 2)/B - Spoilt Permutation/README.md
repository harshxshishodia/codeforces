# B. Spoilt Permutation

**Submission:** https://codeforces.com/contest/56/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya collects coins: he has exactly one coin for every year from 1 to n . Naturally, Vasya keeps all the coins in his collection in the order in which they were released. Once Vasya's younger brother made a change ΓÇö he took all the coins whose release year dated from l to r inclusively and put them in the reverse order. That is, he took a certain segment [ l ,ΓÇë r ] and reversed it. At that the segment's endpoints did not coincide. For example, if n ΓÇë=ΓÇë8 , then initially Vasya's coins were kept in the order 1 2 3 4 5 6 7 8 . If Vasya's younger brother chose the segment [2,ΓÇë6] , then after the reversal the coin order will change to 1 6 5 4 3 2 7 8 . Vasya suspects that someone else could have spoilt the permutation after his brother. Help him to find that out. Check if the given permutation can be obtained from the permutation 1 2 ... n using exactly one segment reversal. If it is possible, find the segment itself.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) which is the number of coins in Vasya's collection. The second line contains space-separated n integers which are the spoilt sequence of coins. It is guaranteed that the given sequence is a permutation, i.e. it contains only integers from 1 to n , and every number is used exactly 1 time.

## Output

If it is impossible to obtain the given permutation from the original one in exactly one action, print 0 0 . Otherwise, print two numbers l r ( 1ΓÇëΓëñΓÇë l ΓÇë<ΓÇë r ΓÇëΓëñΓÇë n ) which are the endpoints of the segment that needs to be reversed to obtain from permutation 1 2 ... n the given one.

## Examples

Example 1:
```
8
1 6 5 4 3 2 7 8
```
```
2 6
```
