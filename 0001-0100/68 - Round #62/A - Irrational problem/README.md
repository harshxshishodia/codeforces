# A. Irrational problem

**Submission:** https://codeforces.com/contest/68/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Little Petya was given this problem for homework:

You are given function (here represents the operation of taking the remainder). His task is to count the number of integers x in range [ a ; b ] with property f ( x )ΓÇë=ΓÇë x .

It is a pity that Petya forgot the order in which the remainders should be taken and wrote down only 4 numbers. Each of 24 possible orders of taking the remainder has equal probability of being chosen. For example, if Petya has numbers 1, 2, 3, 4 then he can take remainders in that order or first take remainder modulo 4, then modulo 2, 3, 1. There also are 22 other permutations of these numbers that represent orders in which remainder can be taken. In this problem 4 numbers wrote down by Petya will be pairwise distinct.

Now it is impossible for Petya to complete the task given by teacher but just for fun he decided to find the number of integers with property that probability that f ( x )ΓÇë=ΓÇë x is not less than 31.4159265352718281828459045% . In other words, Petya will pick up the number x if there exist at least 7 permutations of numbers p 1 ,ΓÇë p 2 ,ΓÇë p 3 ,ΓÇë p 4 , for which f ( x )ΓÇë=ΓÇë x .

## Input

First line of the input will contain 6 integers, separated by spaces: p 1 ,ΓÇë p 2 ,ΓÇë p 3 ,ΓÇë p 4 ,ΓÇë a ,ΓÇë b ( 1ΓÇëΓëñΓÇë p 1 ,ΓÇë p 2 ,ΓÇë p 3 ,ΓÇë p 4 ΓÇëΓëñΓÇë1000,ΓÇë0ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë31415 ). 

It is guaranteed that numbers p 1 ,ΓÇë p 2 ,ΓÇë p 3 ,ΓÇë p 4 will be pairwise distinct.

## Output

Output the number of integers in the given range that have the given property.

## Examples

Example 1:
```
2 7 1 8 2 8
```
```
0
```
