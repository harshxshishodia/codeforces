# E. Two Subsequences

**Submission:** https://codeforces.com/contest/83/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

On an IT lesson Valera studied data compression. The teacher told about a new method, which we shall now describe to you.

Let { a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n } be the given sequence of lines needed to be compressed. Here and below we shall assume that all lines are of the same length and consist only of the digits 0 and 1 . Let's define the compression function:

 
- f ( empty sequence )ΓÇë=ΓÇë empty string 
- f ( s )ΓÇë=ΓÇë s . 
- f ( s 1 ,ΓÇë s 2 )ΓÇë=ΓÇë the smallest in length string, which has one of the prefixes equal to s 1 and one of the suffixes equal to s 2 . For example, f (001,ΓÇë011)ΓÇë=ΓÇë0011 , f (111,ΓÇë011)ΓÇë=ΓÇë111011 . 
- f ( a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n )ΓÇë=ΓÇë f ( f ( a 1 ,ΓÇë a 2 ,ΓÇë a n ΓÇë-ΓÇë1 ),ΓÇë a n ) . For example, f (000,ΓÇë000,ΓÇë111)ΓÇë=ΓÇë f ( f (000,ΓÇë000),ΓÇë111)ΓÇë=ΓÇë f (000,ΓÇë111)ΓÇë=ΓÇë000111 . 

Valera faces a real challenge: he should divide the given sequence { a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n } into two subsequences { b 1 ,ΓÇë b 2 ,ΓÇë...,ΓÇë b k } and { c 1 ,ΓÇë c 2 ,ΓÇë...,ΓÇë c m } , m ΓÇë+ΓÇë k ΓÇë=ΓÇë n , so that the value of S ΓÇë=ΓÇë| f ( b 1 ,ΓÇë b 2 ,ΓÇë...,ΓÇë b k )|ΓÇë+ΓÇë| f ( c 1 ,ΓÇë c 2 ,ΓÇë...,ΓÇë c m )| took the minimum possible value. Here | p | denotes the length of the string p .

Note that it is not allowed to change the relative order of lines in the subsequences. It is allowed to make one of the subsequences empty. Each string from the initial sequence should belong to exactly one subsequence. Elements of subsequences b and c don't have to be consecutive in the original sequence a , i. e. elements of b and c can alternate in a (see samples 2 and 3).

Help Valera to find the minimum possible value of S .

## Input

The first line of input data contains an integer n ΓÇö the number of strings ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë2┬╖10 5 ). Then on n lines follow elements of the sequence ΓÇö strings whose lengths are from 1 to 20 characters, consisting only of digits 0 and 1 . The i ΓÇë+ΓÇë1 -th input line contains the i -th element of the sequence. Elements of the sequence are separated only by a newline. It is guaranteed that all lines have the same length.

## Output

Print a single number ΓÇö the minimum possible value of S .

## Examples

Example 1:
```
3
01
10
01
```
```
4
```

## Note

Detailed answers to the tests:

 
- The best option is to make one of the subsequences empty, and the second one equal to the whole given sequence. | f (01,ΓÇë10,ΓÇë01)|ΓÇë=ΓÇë| f ( f (01,ΓÇë10),ΓÇë01)|ΓÇë=ΓÇë| f (010,ΓÇë01)|ΓÇë=ΓÇë|0101|ΓÇë=ΓÇë4 . 
- The best option is: b ΓÇë=ΓÇë{000,ΓÇë001},ΓÇë c ΓÇë=ΓÇë{111,ΓÇë110}. S ΓÇë=ΓÇë| f (000,ΓÇë001)|ΓÇë+ΓÇë| f (111,ΓÇë110)|ΓÇë=ΓÇë|0001|ΓÇë+ΓÇë|1110|ΓÇë=ΓÇë8 . 
- The best option is: b ΓÇë=ΓÇë{10101,ΓÇë01010,ΓÇë01000},ΓÇë c ΓÇë=ΓÇë{11111,ΓÇë10010}. S ΓÇë=ΓÇë|10101000|ΓÇë+ΓÇë|111110010|ΓÇë=ΓÇë17 .
