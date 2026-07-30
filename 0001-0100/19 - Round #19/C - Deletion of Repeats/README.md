# C. Deletion of Repeats

**Submission:** https://codeforces.com/contest/19/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Once Bob saw a string. It contained so many different letters, that the letters were marked by numbers, but at the same time each letter could be met in the string at most 10 times. Bob didn't like that string, because it contained repeats: a repeat of length x is such a substring of length 2 x , that its first half coincides character by character with its second half. Bob started deleting all the repeats from the string. He does it as follows: while it's possible, Bob takes the shortest repeat, if it is not unique, he takes the leftmost one, and deletes its left half and everything that is to the left of this repeat.

You're given the string seen by Bob. Find out, what it will look like after Bob deletes all the repeats in the way described above.

## Input

The first input line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö length of the string. The following line contains n space-separated integer numbers from 0 to 10 9 inclusive ΓÇö numbers that stand for the letters of the string. It's guaranteed that each letter can be met in the string at most 10 times.

## Output

In the first line output the length of the string's part, left after Bob's deletions. In the second line output all the letters (separated by a space) of the string, left after Bob deleted all the repeats in the described way.

## Examples

Example 1:
```
6
1 2 3 1 2 3
```
```
3
1 2 3
```
