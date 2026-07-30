# D. Interesting Sequence

**Submission:** https://codeforces.com/contest/40/problem/D

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

Berland scientists noticed long ago that the world around them depends on Berland population. Due to persistent research in this area the scientists managed to find out that the Berland chronology starts from the moment when the first two people came to that land (it is considered to have happened in the first year). After one Berland year after the start of the chronology the population had already equaled 13 people (the second year). However, tracing the population number during the following years was an ultimately difficult task, still it was found out that if d i ΓÇö the number of people in Berland in the year of i , then either d i ΓÇë=ΓÇë12 d i ΓÇë-ΓÇë2 , or d i ΓÇë=ΓÇë13 d i ΓÇë-ΓÇë1 ΓÇë-ΓÇë12 d i ΓÇë-ΓÇë2 . Of course no one knows how many people are living in Berland at the moment, but now we can tell if there could possibly be a year in which the country population equaled A . That's what we ask you to determine. Also, if possible, you have to find out in which years it could be (from the beginning of Berland chronology). Let's suppose that it could be in the years of a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a k . Then you have to define how many residents could be in the country during those years apart from the A variant. Look at the examples for further explanation.

## Input

The first line contains integer A ( 1ΓÇëΓëñΓÇë A ΓÇë<ΓÇë10 300 ). It is guaranteed that the number doesn't contain leading zeros.

## Output

On the first output line print YES , if there could be a year in which the total population of the country equaled A , otherwise print NO . 

If the answer is YES , then you also have to print number k ΓÇö the number of years in which the population could equal A . On the next line you have to output precisely k space-separated numbers ΓÇö a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a k . Those numbers have to be output in the increasing order.

On the next line you should output number p ΓÇö how many variants of the number of people could be in the years of a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a k , apart from the A variant. On each of the next p lines you have to print one number ΓÇö the sought number of residents. Those number also have to go in the increasing order. 

If any number (or both of them) k or p exceeds 1000 , then you have to print 1000 instead of it and only the first 1000 possible answers in the increasing order.

The numbers should have no leading zeros.

## Examples

Example 1:
```
2
```
```
YES
1
1
0
```
