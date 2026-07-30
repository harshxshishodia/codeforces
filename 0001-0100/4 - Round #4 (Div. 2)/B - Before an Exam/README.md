# B. Before an Exam

**Submission:** https://codeforces.com/contest/4/problem/B

**Limits:** 0.5 second / 64 megabytes

## Problem Statement

Tomorrow Peter has a Biology exam. He does not like this subject much, but d days ago he learnt that he would have to take this exam. Peter's strict parents made him prepare for the exam immediately, for this purpose he has to study not less than minTime i and not more than maxTime i hours per each i -th day. Moreover, they warned Peter that a day before the exam they would check how he has followed their instructions.

So, today is the day when Peter's parents ask him to show the timetable of his preparatory studies. But the boy has counted only the sum of hours sumTime spent him on preparation, and now he wants to know if he can show his parents a timetable s╤ühedule with d numbers, where each number s╤ühedule i stands for the time in hours spent by Peter each i -th day on biology studies, and satisfying the limitations imposed by his parents, and at the same time the sum total of all schedule i should equal to sumTime .

## Input

The first input line contains two integer numbers d ,ΓÇë sumTime ( 1ΓÇëΓëñΓÇë d ΓÇëΓëñΓÇë30,ΓÇë0ΓÇëΓëñΓÇë sumTime ΓÇëΓëñΓÇë240 ) ΓÇö the amount of days, during which Peter studied, and the total amount of hours, spent on preparation. Each of the following d lines contains two integer numbers minTime i ,ΓÇë maxTime i ( 0ΓÇëΓëñΓÇë minTime i ΓÇëΓëñΓÇë maxTime i ΓÇëΓëñΓÇë8 ), separated by a space ΓÇö minimum and maximum amount of hours that Peter could spent in the i -th day.

## Output

In the first line print YES , and in the second line print d numbers (separated by a space), each of the numbers ΓÇö amount of hours, spent by Peter on preparation in the corresponding day, if he followed his parents' instructions; or print NO in the unique line. If there are many solutions, print any of them.

## Examples

Example 1:
```
1 48
5 7
```
```
NO
```
