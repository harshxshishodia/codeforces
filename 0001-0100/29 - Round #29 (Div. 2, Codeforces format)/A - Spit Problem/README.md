# A. Spit Problem

**Submission:** https://codeforces.com/contest/29/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

In a Berland's zoo there is an enclosure with camels. It is known that camels like to spit. Bob watched these interesting animals for the whole day and registered in his notepad where each animal spitted. Now he wants to know if in the zoo there are two camels, which spitted at each other. Help him to solve this task.

The trajectory of a camel's spit is an arc, i.e. if the camel in position x spits d meters right, he can hit only the camel in position x ΓÇë+ΓÇë d , if such a camel exists.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the amount of camels in the zoo. Each of the following n lines contains two integers x i and d i ( ΓÇë-ΓÇë10 4 ΓÇëΓëñΓÇë x i ΓÇëΓëñΓÇë10 4 ,ΓÇë1ΓÇëΓëñΓÇë| d i |ΓÇëΓëñΓÇë2┬╖10 4 ) ΓÇö records in Bob's notepad. x i is a position of the i -th camel, and d i is a distance at which the i -th camel spitted. Positive values of d i correspond to the spits right, negative values correspond to the spits left. No two camels may stand in the same position.

## Output

If there are two camels, which spitted at each other, output YES . Otherwise, output NO .

## Examples

Example 1:
```
2
0 1
1 -1
```
```
YES
```
