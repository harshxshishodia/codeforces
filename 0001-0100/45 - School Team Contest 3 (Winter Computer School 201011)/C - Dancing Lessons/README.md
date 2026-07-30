# C. Dancing Lessons

**Submission:** https://codeforces.com/contest/45/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There are n people taking dancing lessons. Every person is characterized by his/her dancing skill a i . At the beginning of the lesson they line up from left to right. While there is at least one couple of a boy and a girl in the line, the following process is repeated: the boy and girl who stand next to each other, having the minimal difference in dancing skills start to dance. If there are several such couples, the one first from the left starts to dance. After a couple leaves to dance, the line closes again, i.e. as a result the line is always continuous. The difference in dancing skills is understood as the absolute value of difference of a i variable. Your task is to find out what pairs and in what order will start dancing.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë2┬╖10 5 ) ΓÇö the number of people. The next line contains n symbols B or G without spaces. B stands for a boy, G stands for a girl. The third line contains n space-separated integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 7 ) ΓÇö the dancing skill. People are specified from left to right in the order in which they lined up.

## Output

Print the resulting number of couples k . Then print k lines containing two numerals each ΓÇö the numbers of people forming the couple. The people are numbered with integers from 1 to n from left to right. When a couple leaves to dance you shouldn't renumber the people. The numbers in one couple should be sorted in the increasing order. Print the couples in the order in which they leave to dance.

## Examples

Example 1:
```
4
BGBG
4 2 4 3
```
```
2
3 4
1 2
```
