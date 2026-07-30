# A. Goshtasp, Vishtasp and Eidi

**Submission:** https://codeforces.com/contest/72/problem/A

**Limits:** 5 seconds / 256 megabytes

## Problem Statement

Goshtasp was known to be a good programmer in his school. One day Vishtasp, Goshtasp's friend, asked him to solve this task:

 Given a positive integer n , you should determine whether n is rich. 

The positive integer x is rich, if there exists some set of distinct numbers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a m such that . In addition: every a i should be either a prime number, or equal to 1 .

Vishtasp said that he would share his Eidi 50ΓÇë/ΓÇë50 with Goshtasp, if he could solve the task. Eidi is money given to children for Noruz by their parents and/or relatives.

Goshtasp needs to solve this problem to get money, you need to solve it to get score!

## Input

Input contains a single positive integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10000 ).

## Output

If the number is not rich print 0 . Otherwise print the numbers a 1 ,ΓÇë...,ΓÇë a m . If several solutions exist print the lexicographically latest solution. Answers are compared as sequences of numbers, not as strings.

For comparing two sequences a 1 ,ΓÇë...,ΓÇë a m and b 1 ,ΓÇë...,ΓÇë b n we first find the first index i such that a i ΓÇëΓëáΓÇë b i , if a i ΓÇë<ΓÇë b i then a is lexicographically earlier and if b i ΓÇë<ΓÇë a i then b is lexicographically earlier. If m ΓÇëΓëáΓÇë n we add zeroes at the end of the smaller sequence (only for the moment of comparison) and then perform the comparison.

You do not need to minimize the number of elements in sequence (i.e. m ). You just need to print the lexicographically latest solution.

See samples to find out how to print the sequence.

## Examples

Example 1:
```
11
```
```
11=11
```
