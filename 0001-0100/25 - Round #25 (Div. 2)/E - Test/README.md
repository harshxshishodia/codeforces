# E. Test

**Submission:** https://codeforces.com/contest/25/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Sometimes it is hard to prepare tests for programming problems. Now Bob is preparing tests to new problem about strings ΓÇö input data to his problem is one string. Bob has 3 wrong solutions to this problem. The first gives the wrong answer if the input data contains the substring s 1 , the second enters an infinite loop if the input data contains the substring s 2 , and the third requires too much memory if the input data contains the substring s 3 . Bob wants these solutions to fail single test. What is the minimal length of test, which couldn't be passed by all three Bob's solutions?

## Input

There are exactly 3 lines in the input data. The i -th line contains string s i . All the strings are non-empty, consists of lowercase Latin letters, the length of each string doesn't exceed 10 5 .

## Output

Output one number ΓÇö what is minimal length of the string, containing s 1 , s 2 and s 3 as substrings.

## Examples

Example 1:
```
ab
bc
cd
```
```
4
```
