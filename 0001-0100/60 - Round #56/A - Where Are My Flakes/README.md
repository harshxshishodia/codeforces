# A. Where Are My Flakes?

**Submission:** https://codeforces.com/contest/60/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One morning the Cereal Guy found out that all his cereal flakes were gone. He found a note instead of them. It turned out that his smart roommate hid the flakes in one of n boxes. The boxes stand in one row, they are numbered from 1 to n from the left to the right. The roommate left hints like "Hidden to the left of the i -th box" (" To the left of i "), "Hidden to the right of the i -th box" (" To the right of i "). Such hints mean that there are no flakes in the i -th box as well. The Cereal Guy wants to know the minimal number of boxes he necessarily needs to check to find the flakes considering all the hints. Or he wants to find out that the hints are contradictory and the roommate lied to him, that is, no box has the flakes.

## Input

The first line contains two integers n and m ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000,ΓÇë0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë1000 ) which represent the number of boxes and the number of hints correspondingly. Next m lines contain hints like " To the left of i " and " To the right of i ", where i is integer ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ). The hints may coincide.

## Output

The answer should contain exactly one integer ΓÇö the number of boxes that should necessarily be checked or " -1 " if the hints are contradictory.

## Examples

Example 1:
```
2 1
To the left of 2
```
```
1
```
