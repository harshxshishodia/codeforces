# B. Blog Photo

**Submission:** https://codeforces.com/contest/53/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One popular blog site edits the uploaded photos like this. It cuts a rectangular area out of them so that the ratio of height to width (i.e. the height ΓÇë/ΓÇë width quotient) can vary from 0.8 to 1.25 inclusively. Besides, at least one side of the cut area should have a size, equal to some power of number 2 ( 2 x for some integer x ). If those rules don't indicate the size of the cut are clearly, then the way with which the cut part possesses the largest area is chosen. Of course, both sides of the cut area should be integer. If there are several answers to this problem, you should choose the answer with the maximal height.

## Input

The first line contains a pair of integers h and w ( 1ΓÇëΓëñΓÇë h ,ΓÇë w ΓÇëΓëñΓÇë10 9 ) which are the height and width of the uploaded photo in pixels.

## Output

Print two integers which are the height and width of the cut area.

## Examples

Example 1:
```
2 1
```
```
1 1
```
