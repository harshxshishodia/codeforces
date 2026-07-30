# D. Changing a String

**Submission:** https://codeforces.com/contest/56/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There is a string s , consisting of capital Latin letters. Let's denote its current length as | s | . During one move it is allowed to apply one of the following operations to it: 

 
- INSERT pos ch ΓÇö insert a letter ch in the string s in the position pos ( 1ΓÇëΓëñΓÇë pos ΓÇëΓëñΓÇë| s |ΓÇë+ΓÇë1,ΓÇë A ΓÇëΓëñΓÇë ch ΓÇëΓëñΓÇë Z ). The letter ch becomes the pos -th symbol of the string s , at that the letters shift aside and the length of the string increases by 1. 
- DELETE pos ΓÇö delete a character number pos ( 1ΓÇëΓëñΓÇë pos ΓÇëΓëñΓÇë| s | ) from the string s . At that the letters shift together and the length of the string decreases by 1. 
- REPLACE pos ch ΓÇö the letter in the position pos of the line s is replaced by ch ( 1ΓÇëΓëñΓÇë pos ΓÇëΓëñΓÇë| s |,ΓÇë A ΓÇëΓëñΓÇë ch ΓÇëΓëñΓÇë Z ). At that the length of the string does not change. 

Your task is to find in which minimal number of moves one can get a t string from an s string. You should also find the sequence of actions leading to the required results.

## Input

The first line contains s , the second line contains t . The lines consist only of capital Latin letters, their lengths are positive numbers from 1 to 1000 .

## Output

In the first line print the number of moves k in the given sequence of operations. The number should be the minimal possible one. Then print k lines containing one operation each. Print the operations in the format, described above. If there are several solutions, print any of them.

## Examples

Example 1:
```
ABA
ABBBA
```
```
2
INSERT 3 B
INSERT 4 B
```
