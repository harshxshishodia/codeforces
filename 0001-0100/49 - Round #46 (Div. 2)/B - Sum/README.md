# B. Sum

**Submission:** https://codeforces.com/contest/49/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya studies positional numeral systems. Unfortunately, he often forgets to write the base of notation in which the expression is written. Once he saw a note in his notebook saying a ΓÇë+ΓÇë b ΓÇë=ΓÇë? , and that the base of the positional notation wasnΓÇÖt written anywhere. Now Vasya has to choose a base p and regard the expression as written in the base p positional notation. Vasya understood that he can get different results with different bases, and some bases are even invalid. For example, expression 78ΓÇë+ΓÇë87 in the base 16 positional notation is equal to FF 16 , in the base 15 positional notation it is equal to 110 15 , in the base 10 one ΓÇö to 165 10 , in the base 9 one ΓÇö to 176 9 , and in the base 8 or lesser-based positional notations the expression is invalid as all the numbers should be strictly less than the positional notation base. Vasya got interested in what is the length of the longest possible expression value. Help him to find this length.

The length of a number should be understood as the number of numeric characters in it. For example, the length of the longest answer for 78ΓÇë+ΓÇë87ΓÇë=ΓÇë? is 3. It is calculated like that in the base 15 ( 110 15 ), base 10 ( 165 10 ), base 9 ( 176 9 ) positional notations, for example, and in some other ones.

## Input

The first letter contains two space-separated numbers a and b ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ΓÇëΓëñΓÇë1000 ) which represent the given summands.

## Output

Print a single number ΓÇö the length of the longest answer.

## Examples

Example 1:
```
78 87
```
```
3
```
