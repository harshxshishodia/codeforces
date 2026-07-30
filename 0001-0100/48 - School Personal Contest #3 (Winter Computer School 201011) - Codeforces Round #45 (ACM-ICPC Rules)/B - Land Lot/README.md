# B. Land Lot

**Submission:** https://codeforces.com/contest/48/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya has a beautiful garden where wonderful fruit trees grow and yield fantastic harvest every year. But lately thieves started to sneak into the garden at nights and steal the fruit too often. Vasya canΓÇÖt spend the nights in the garden and guard the fruit because thereΓÇÖs no house in the garden! Vasya had been saving in for some time and finally he decided to build the house. The rest is simple: he should choose in which part of the garden to build the house. In the evening he sat at his table and drew the gardenΓÇÖs plan. On the plan the garden is represented as a rectangular checkered field n ΓÇë├ùΓÇë m in size divided into squares whose side length is 1. In some squares Vasya marked the trees growing there (one shouldnΓÇÖt plant the trees too close to each other thatΓÇÖs why one square contains no more than one tree). Vasya wants to find a rectangular land lot a ΓÇë├ùΓÇë b squares in size to build a house on, at that the land lot border should go along the lines of the grid that separates the squares. All the trees that grow on the building lot will have to be chopped off. Vasya loves his garden very much, so help him choose the building land lot location so that the number of chopped trees would be as little as possible.

## Input

The first line contains two integers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë50 ) which represent the garden location. The next n lines contain m numbers 0 or 1, which describe the garden on the scheme. The zero means that a tree doesnΓÇÖt grow on this square and the 1 means that there is a growing tree. The last line contains two integers a and b ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ΓÇëΓëñΓÇë50 ). Note that Vasya can choose for building an a ΓÇë├ùΓÇë b rectangle as well a b ΓÇë├ùΓÇë a one, i.e. the side of the lot with the length of a can be located as parallel to the garden side with the length of n , as well as parallel to the garden side with the length of m .

## Output

Print the minimum number of trees that needs to be chopped off to select a land lot a ΓÇë├ùΓÇë b in size to build a house on. It is guaranteed that at least one lot location can always be found, i. e. either a ΓÇëΓëñΓÇë n and b ΓÇëΓëñΓÇë m , or a ΓÇëΓëñΓÇë m ╨╕ b ΓÇëΓëñΓÇë n .

## Examples

Example 1:
```
2 2
1 0
1 1
1 1
```
```
0
```

## Note

In the second example the upper left square is (1,1) and the lower right is (3,2).
