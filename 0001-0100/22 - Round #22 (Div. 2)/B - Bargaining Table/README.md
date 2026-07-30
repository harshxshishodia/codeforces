# B. Bargaining Table

**Submission:** https://codeforces.com/contest/22/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Bob wants to put a new bargaining table in his office. To do so he measured the office room thoroughly and drew its plan: Bob's office room is a rectangular room n ΓÇë├ùΓÇë m meters. Each square meter of the room is either occupied by some furniture, or free. A bargaining table is rectangular, and should be placed so, that its sides are parallel to the office walls. Bob doesn't want to change or rearrange anything, that's why all the squares that will be occupied by the table should be initially free. Bob wants the new table to sit as many people as possible, thus its perimeter should be maximal. Help Bob find out the maximum possible perimeter of a bargaining table for his office.

## Input

The first line contains 2 space-separated numbers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë25 ) ΓÇö the office room dimensions. Then there follow n lines with m characters 0 or 1 each. 0 stands for a free square meter of the office room. 1 stands for an occupied square meter. It's guaranteed that at least one square meter in the room is free.

## Output

Output one number ΓÇö the maximum possible perimeter of a bargaining table for Bob's office room.

## Examples

Example 1:
```
3 3
000
010
000
```
```
8
```
