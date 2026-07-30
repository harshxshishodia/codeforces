# C. Stripe 2

**Submission:** https://codeforces.com/contest/21/problem/C

**Limits:** 1 second / 64 megabytes

## Problem Statement

Once Bob took a paper stripe of n squares (the height of the stripe is 1 square). In each square he wrote an integer number, possibly negative. He became interested in how many ways exist to cut this stripe into three pieces so that the sum of numbers from each piece is equal to the sum of numbers from any other piece, and each piece contains positive integer amount of squares. Would you help Bob solve this problem?

## Input

The first input line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö amount of squares in the stripe. The second line contains n space-separated numbers ΓÇö they are the numbers written in the squares of the stripe. These numbers are integer and do not exceed 10000 in absolute value.

## Output

Output the amount of ways to cut the stripe into three non-empty pieces so that the sum of numbers from each piece is equal to the sum of numbers from any other piece. Don't forget that it's allowed to cut the stripe along the squares' borders only.

## Examples

Example 1:
```
4
1 2 3 3
```
```
1
```
