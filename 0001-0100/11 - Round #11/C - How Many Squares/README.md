# C. How Many Squares?

**Submission:** https://codeforces.com/contest/11/problem/C

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

You are given a 0-1 rectangular matrix. What is the number of squares in it? A square is a solid square frame (border) with linewidth equal to 1. A square should be at least 2ΓÇë├ùΓÇë2 . We are only interested in two types of squares: 

 
- squares with each side parallel to a side of the matrix; 
- squares with each side parallel to a diagonal of the matrix. 
 
For example the following matrix contains only one square of the first type: 
0000000 
0111100 
0100100 
0100100 
0111100
 
The following matrix contains only one square of the second type:
0000000
0010000
0101000
0010000
0000000
 
Regardless of type, a square must contain at least one 1 and can't touch (by side or corner) any foreign 1 . Of course, the lengths of the sides of each square should be equal.

How many squares are in the given matrix?

## Input

The first line contains integer t ( 1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë10000 ), where t is the number of test cases in the input. Then test cases follow. Each case starts with a line containing integers n and m ( 2ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë250 ), where n is the number of rows and m is the number of columns. The following n lines contain m characters each ( 0 or 1 ).

The total number of characters in all test cases doesn't exceed 10 6 for any input file.

## Output

You should output exactly t lines, with the answer to the i -th test case on the i -th line.

## Examples

Example 1:
```
2
8 8
00010001
00101000
01000100
10000010
01000100
00101000
11010011
11000011
10 10
1111111000
1000001000
1011001000
1011001010
1000001101
1001001010
1010101000
1001001000
1000001000
1111111000
```
```
1
2
```
