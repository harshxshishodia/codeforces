# C. Trees

**Submission:** https://codeforces.com/contest/58/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

On Bertown's main street n trees are growing, the tree number i has the height of a i meters ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ). By the arrival of the President of Berland these trees were decided to be changed so that their heights formed a beautiful sequence. This means that the heights of trees on ends (the 1 st one and the n -th one) should be equal to each other, the heights of the 2 -nd and the ( n ΓÇë-ΓÇë1) -th tree must also be equal to each other, at that the height of the 2 -nd tree should be larger than the height of the first tree by 1 , and so on. In other words, the heights of the trees, standing at equal distance from the edge (of one end of the sequence) must be equal to each other, and with the increasing of the distance from the edge by 1 the tree height must also increase by 1 . For example, the sequences " 2 3 4 5 5 4 3 2 " and " 1 2 3 2 1 " are beautiful, and ' 1 3 3 1 " and " 1 2 3 1 " are not. 

Changing the height of a tree is a very expensive operation, using advanced technologies invented by Berland scientists. In one operation you can choose any tree and change its height to any number, either increase or decrease. Note that even after the change the height should remain a positive integer, i. e, it can't be less than or equal to zero. Identify the smallest number of changes of the trees' height needed for the sequence of their heights to become beautiful.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) which is the number of trees. The second line contains integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 5 ) which are the heights of the trees.

## Output

Print a single number which is the minimal number of trees whose heights will have to be changed for the sequence to become beautiful.

## Examples

Example 1:
```
3
2 2 2
```
```
1
```
