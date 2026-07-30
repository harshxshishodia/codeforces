# B. Hierarchy

**Submission:** https://codeforces.com/contest/17/problem/B

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

Nick's company employed n people. Now Nick needs to build a tree hierarchy of ┬½supervisor-surbodinate┬╗ relations in the company (this is to say that each employee, except one, has exactly one supervisor). There are m applications written in the following form: ┬½employee a i is ready to become a supervisor of employee b i at extra cost c i ┬╗ . The qualification q j of each employee is known, and for each application the following is true: q a i ΓÇë>ΓÇë q b i . 

Would you help Nick calculate the minimum cost of such a hierarchy, or find out that it is impossible to build it.

## Input

The first input line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) ΓÇö amount of employees in the company. The following line contains n space-separated numbers q j ( 0ΓÇëΓëñΓÇë q j ΓÇëΓëñΓÇë10 6 )ΓÇö the employees' qualifications. The following line contains number m ( 0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10000 ) ΓÇö amount of received applications. The following m lines contain the applications themselves, each of them in the form of three space-separated numbers: a i , b i and c i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n , 0ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë10 6 ). Different applications can be similar, i.e. they can come from one and the same employee who offered to become a supervisor of the same person but at a different cost. For each application q a i ΓÇë>ΓÇë q b i .

## Output

Output the only line ΓÇö the minimum cost of building such a hierarchy, or -1 if it is impossible to build it.

## Examples

Example 1:
```
4
7 2 3 1
4
1 2 5
2 4 1
3 4 1
1 3 5
```
```
11
```

## Note

In the first sample one of the possible ways for building a hierarchy is to take applications with indexes 1, 2 and 4, which give 11 as the minimum total cost. In the second sample it is impossible to build the required hierarchy, so the answer is -1 .
