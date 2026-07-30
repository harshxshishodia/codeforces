# D. Queue

**Submission:** https://codeforces.com/contest/92/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There are n walruses standing in a queue in an airport. They are numbered starting from the queue's tail: the 1 -st walrus stands at the end of the queue and the n -th walrus stands at the beginning of the queue. The i -th walrus has the age equal to a i .

The i -th walrus becomes displeased if there's a younger walrus standing in front of him, that is, if exists such j ( i ΓÇë<ΓÇë j ), that a i ΓÇë>ΓÇë a j . The displeasure of the i -th walrus is equal to the number of walruses between him and the furthest walrus ahead of him, which is younger than the i -th one. That is, the further that young walrus stands from him, the stronger the displeasure is.

The airport manager asked you to count for each of n walruses in the queue his displeasure.

## Input

The first line contains an integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö the number of walruses in the queue. The second line contains integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ).

Note that some walruses can have the same age but for the displeasure to emerge the walrus that is closer to the head of the queue needs to be strictly younger than the other one.

## Output

Print n numbers: if the i -th walrus is pleased with everything, print "-1" (without the quotes). Otherwise, print the i -th walrus's displeasure: the number of other walruses that stand between him and the furthest from him younger walrus.

## Examples

Example 1:
```
6
10 8 5 3 50 45
```
```
2 1 0 -1 0 -1
```
