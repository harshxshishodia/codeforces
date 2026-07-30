# E. Square Equation Roots

**Submission:** https://codeforces.com/contest/50/problem/E

**Limits:** 5 seconds / 256 megabytes

## Problem Statement

A schoolboy Petya studies square equations. The equations that are included in the school curriculum, usually look simple: 
 x 2 ΓÇë+ΓÇë2 bx ΓÇë+ΓÇë c ΓÇë=ΓÇë0 where b , c are natural numbers.
Petya noticed that some equations have two real roots, some of them have only one root and some equations don't have real roots at all. Moreover it turned out that several different square equations can have a common root.

Petya is interested in how many different real roots have all the equations of the type described above for all the possible pairs of numbers b and c such that 1ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë n , 1ΓÇëΓëñΓÇë c ΓÇëΓëñΓÇë m . Help Petya find that number.

## Input

The single line contains two integers n and m . ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë5000000 ).

## Output

Print a single number which is the number of real roots of the described set of equations.

## Examples

Example 1:
```
3 3
```
```
12
```

## Note

In the second test from the statement the following equations are analysed:

 b ΓÇë=ΓÇë1 , c ΓÇë=ΓÇë1 : x 2 ΓÇë+ΓÇë2 x ΓÇë+ΓÇë1ΓÇë=ΓÇë0 ; The root is x ΓÇë=ΓÇëΓÇë-ΓÇë1 

 b ΓÇë=ΓÇë1 , c ΓÇë=ΓÇë2 : x 2 ΓÇë+ΓÇë2 x ΓÇë+ΓÇë2ΓÇë=ΓÇë0 ; No roots

 Overall there's one root

In the second test the following equations are analysed:

 b ΓÇë=ΓÇë1 , c ΓÇë=ΓÇë1 : x 2 ΓÇë+ΓÇë2 x ΓÇë+ΓÇë1ΓÇë=ΓÇë0 ; The root is x ΓÇë=ΓÇëΓÇë-ΓÇë1 

 b ΓÇë=ΓÇë1 , c ΓÇë=ΓÇë2 : x 2 ΓÇë+ΓÇë2 x ΓÇë+ΓÇë2ΓÇë=ΓÇë0 ; No roots

 b ΓÇë=ΓÇë1 , c ΓÇë=ΓÇë3 : x 2 ΓÇë+ΓÇë2 x ΓÇë+ΓÇë3ΓÇë=ΓÇë0 ; No roots

 b ΓÇë=ΓÇë2 , c ΓÇë=ΓÇë1 : x 2 ΓÇë+ΓÇë4 x ΓÇë+ΓÇë1ΓÇë=ΓÇë0 ; The roots are 

 b ΓÇë=ΓÇë2 , c ΓÇë=ΓÇë2 : x 2 ΓÇë+ΓÇë4 x ΓÇë+ΓÇë2ΓÇë=ΓÇë0 ; The roots are 

 b ΓÇë=ΓÇë2 , c ΓÇë=ΓÇë3 : x 2 ΓÇë+ΓÇë4 x ΓÇë+ΓÇë3ΓÇë=ΓÇë0 ; The roots are x 1 ΓÇë=ΓÇëΓÇë-ΓÇë3,ΓÇë x 2 ΓÇë=ΓÇëΓÇë-ΓÇë1 

 b ΓÇë=ΓÇë3 , c ΓÇë=ΓÇë1 : x 2 ΓÇë+ΓÇë6 x ΓÇë+ΓÇë1ΓÇë=ΓÇë0 ; The roots are 

 b ΓÇë=ΓÇë3 , c ΓÇë=ΓÇë2 : x 2 ΓÇë+ΓÇë6 x ΓÇë+ΓÇë2ΓÇë=ΓÇë0 ; The roots are 

 b ΓÇë=ΓÇë3 , c ΓÇë=ΓÇë3 : x 2 ΓÇë+ΓÇë6 x ΓÇë+ΓÇë3ΓÇë=ΓÇë0 ; The roots are Overall there are 13 roots and as the root ΓÇë-ΓÇë1 is repeated twice, that means there are 12 different roots.
