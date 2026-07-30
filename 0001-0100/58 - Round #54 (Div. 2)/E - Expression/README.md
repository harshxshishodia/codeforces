# E. Expression

**Submission:** https://codeforces.com/contest/58/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One day Vasya was solving arithmetical problems. He wrote down an expression a ΓÇë+ΓÇë b ΓÇë=ΓÇë c in his notebook. When the teacher checked Vasya's work it turned out that Vasya had solved the problem incorrectly. Now Vasya tries to find excuses. He says that he simply forgot to write down several digits in numbers a , b and c , but he can't remember what numbers they actually were. Help Vasya, find such numbers x , y and z , with which the following conditions are met: 

 
- x ΓÇë+ΓÇë y ΓÇë=ΓÇë z , 
- from the expression x ΓÇë+ΓÇë y ΓÇë=ΓÇë z several digits can be erased in such a way that the result will be a ΓÇë+ΓÇë b ΓÇë=ΓÇë c , 
- the expression x ΓÇë+ΓÇë y ΓÇë=ΓÇë z should have the minimal length.

## Input

The first and only input line contains the expression a ΓÇë+ΓÇë b ΓÇë=ΓÇë c ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ,ΓÇë c ΓÇëΓëñΓÇë10 6 , a , b and c don't contain leading zeroes) which is the expression Vasya wrote down.

## Output

Print the correct expression x ΓÇë+ΓÇë y ΓÇë=ΓÇë z ( x , y and z are non-negative numbers without leading zeroes). The expression a ΓÇë+ΓÇë b ΓÇë=ΓÇë c must be met in x ΓÇë+ΓÇë y ΓÇë=ΓÇë z as a subsequence. The printed solution should have the minimal possible number of characters. If there are several such solutions, you can print any of them.

## Examples

Example 1:
```
2+4=5
```
```
21+4=25
```
