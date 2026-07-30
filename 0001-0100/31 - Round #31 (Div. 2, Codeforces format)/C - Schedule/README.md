# C. Schedule

**Submission:** https://codeforces.com/contest/31/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

At the beginning of the new semester there is new schedule in the Berland State University. According to this schedule, n groups have lessons at the room 31. For each group the starting time of the lesson and the finishing time of the lesson are known. It has turned out that it is impossible to hold all lessons, because for some groups periods of their lessons intersect. If at some moment of time one groups finishes it's lesson, and the other group starts the lesson, their lessons don't intersect.

The dean wants to cancel the lesson in one group so that no two time periods of lessons of the remaining groups intersect. You are to find all ways to do that.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë5000 ) ΓÇö amount of groups, which have lessons in the room 31. Then n lines follow, each of them contains two integers l i r i ( 1ΓÇëΓëñΓÇë l i ΓÇë<ΓÇë r i ΓÇëΓëñΓÇë10 6 ) ΓÇö starting and finishing times of lesson of the i -th group. It is possible that initially no two lessons intersect (see sample 1).

## Output

Output integer k ΓÇö amount of ways to cancel the lesson in exactly one group so that no two time periods of lessons of the remaining groups intersect. In the second line output k numbers ΓÇö indexes of groups, where it is possible to cancel the lesson. Groups are numbered starting from 1 in the order that they were given in the input. Output the numbers in increasing order.

## Examples

Example 1:
```
3
3 10
20 30
1 3
```
```
3
1 2 3
```
