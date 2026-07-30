# F. Polynom

**Submission:** https://codeforces.com/contest/100/problem/F

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

You are given a polynom in form p ( x )ΓÇë=ΓÇë( x ΓÇë+ΓÇë a 1 )┬╖( x ΓÇë+ΓÇë a 2 )┬╖... ( x ΓÇë+ΓÇë a n ) . Write Pike program to print it in a standard form p ( x )ΓÇë=ΓÇë x n ΓÇë+ΓÇë b 1 x n ΓÇë-ΓÇë1 ΓÇë+ΓÇë...ΓÇë+ΓÇë b n ΓÇë-ΓÇë1 x ΓÇë+ΓÇë b n . You should write each addend in form ┬½ C*X^K ┬╗ (for example, 5*X^8 ).

Please, write the polynom in the shortest way, so you should skip unnecessary terms: some terms ┬½ C*X^K ┬╗ should be reduced or even omitted. Look for the samples for clarification.

## Input

The first line of the input contains n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë9 ). The following n lines contain integer a i ( ΓÇë-ΓÇë10ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 ).

## Output

Print the given polynom in a standard way. Note, that the answer in this problem response uniquely determined.

## Examples

Example 1:
```
2
-1
1
```
```
X^2-1
```
