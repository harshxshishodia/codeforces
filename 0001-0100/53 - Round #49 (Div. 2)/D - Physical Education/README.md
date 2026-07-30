# D. Physical Education

**Submission:** https://codeforces.com/contest/53/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya is a school PE teacher. Unlike other PE teachers, Vasya doesn't like it when the students stand in line according to their height. Instead, he demands that the children stand in the following order: a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n , where a i is the height of the i -th student in the line and n is the number of students in the line. The children find it hard to keep in mind this strange arrangement, and today they formed the line in the following order: b 1 ,ΓÇë b 2 ,ΓÇë...,ΓÇë b n , which upset Vasya immensely. Now Vasya wants to rearrange the children so that the resulting order is like this: a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n . During each move Vasya can swap two people who stand next to each other in the line. Help Vasya, find the sequence of swaps leading to the arrangement Vasya needs. It is not required to minimize the number of moves.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë300 ) which is the number of students. The second line contains n space-separated integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ) which represent the height of the student occupying the i -th place must possess. The third line contains n space-separated integers b i ( 1ΓÇëΓëñΓÇë b i ΓÇëΓëñΓÇë10 9 ) which represent the height of the student occupying the i -th place in the initial arrangement. It is possible that some students possess similar heights. It is guaranteed that it is possible to arrange the children in the required order, i.e. a and b coincide as multisets.

## Output

In the first line print an integer k ( 0ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë10 6 ) which is the number of moves. It is not required to minimize k but it must not exceed 10 6 . Then print k lines each containing two space-separated integers. Line p i , p i ΓÇë+ΓÇë1 ( 1ΓÇëΓëñΓÇë p i ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1 ) means that Vasya should swap students occupying places p i and p i ΓÇë+ΓÇë1 .

## Examples

Example 1:
```
4
1 2 3 2
3 2 1 2
```
```
4
2 3
1 2
3 4
2 3
```
