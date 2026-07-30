# B. pSort

**Submission:** https://codeforces.com/contest/28/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One day n cells of some array decided to play the following game. Initially each cell contains a number which is equal to it's ordinal number (starting from 1 ). Also each cell determined it's favourite number. On it's move i -th cell can exchange it's value with the value of some other j -th cell, if | i ΓÇë-ΓÇë j |ΓÇë=ΓÇë d i , where d i is a favourite number of i -th cell. Cells make moves in any order, the number of moves is unlimited.

The favourite number of each cell will be given to you. You will also be given a permutation of numbers from 1 to n . You are to determine whether the game could move to this state.

## Input

The first line contains positive integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the number of cells in the array. The second line contains n distinct integers from 1 to n ΓÇö permutation. The last line contains n integers from 1 to n ΓÇö favourite numbers of the cells.

## Output

If the given state is reachable in the described game, output YES , otherwise NO .

## Examples

Example 1:
```
5
5 4 3 2 1
1 1 1 1 1
```
```
YES
```
