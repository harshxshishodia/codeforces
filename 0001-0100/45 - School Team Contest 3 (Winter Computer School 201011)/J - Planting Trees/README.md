# J. Planting Trees

**Submission:** https://codeforces.com/contest/45/problem/J

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya is a Greencode wildlife preservation society proponent. One day he found an empty field nobody owned, divided it into n ΓÇë├ùΓÇë m squares and decided to plant a forest there. Vasya will plant nm trees of all different heights from 1 to nm . For his forest to look more natural he wants any two trees growing in the side neighbouring squares to have the absolute value of difference in heights to be strictly more than 1. Help Vasya: make the plan of the forest planting for which this condition is fulfilled.

## Input

The first line contains two space-separated integers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë100 ) ΓÇö the number of rows and columns on Vasya's field

## Output

If there's no solution, print -1 . Otherwise, print n lines containing m numbers each ΓÇö the trees' planting plan. In every square of the plan the height of a tree that should be planted on this square should be written. If there are several solutions to that problem, print any of them.

## Examples

Example 1:
```
2 3
```
```
3 6 2
5 1 4
```
