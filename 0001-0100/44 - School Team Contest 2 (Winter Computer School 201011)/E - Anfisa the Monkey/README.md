# E. Anfisa the Monkey

**Submission:** https://codeforces.com/contest/44/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Anfisa the monkey learns to type. She is yet unfamiliar with the "space" key and can only type in lower-case Latin letters. Having typed for a fairly long line, Anfisa understood that it would be great to divide what she has written into k lines not shorter than a and not longer than b , for the text to resemble human speech more. Help Anfisa.

## Input

The first line contains three integers k , a and b ( 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë200 , 1ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë200 ). The second line contains a sequence of lowercase Latin letters ΓÇö the text typed by Anfisa. It is guaranteed that the given line is not empty and its length does not exceed 200 symbols.

## Output

Print k lines, each of which contains no less than a and no more than b symbols ΓÇö Anfisa's text divided into lines. It is not allowed to perform any changes in the text, such as: deleting or adding symbols, changing their order, etc. If the solution is not unique, print any of them. If there is no solution, print "No solution" (without quotes).

## Examples

Example 1:
```
3 2 5
abrakadabra
```
```
ab
rakad
abra
```
