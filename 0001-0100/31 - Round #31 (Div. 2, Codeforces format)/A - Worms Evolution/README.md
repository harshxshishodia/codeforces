# A. Worms Evolution

**Submission:** https://codeforces.com/contest/31/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Professor Vasechkin is studying evolution of worms. Recently he put forward hypotheses that all worms evolve by division. There are n forms of worms. Worms of these forms have lengths a 1 , a 2 , ..., a n . To prove his theory, professor needs to find 3 different forms that the length of the first form is equal to sum of lengths of the other two forms. Help him to do this.

## Input

The first line contains integer n ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö amount of worm's forms. The second line contains n space-separated integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë1000 ) ΓÇö lengths of worms of each form.

## Output

Output 3 distinct integers i j k ( 1ΓÇëΓëñΓÇë i ,ΓÇë j ,ΓÇë k ΓÇëΓëñΓÇë n ) ΓÇö such indexes of worm's forms that a i ΓÇë=ΓÇë a j ΓÇë+ΓÇë a k . If there is no such triple, output -1 . If there are several solutions, output any of them. It possible that a j ΓÇë=ΓÇë a k .

## Examples

Example 1:
```
5
1 2 3 5 7
```
```
3 2 1
```
