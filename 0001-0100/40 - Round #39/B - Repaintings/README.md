# B. Repaintings

**Submission:** https://codeforces.com/contest/40/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

A chessboard n ΓÇë├ùΓÇë m in size is given. During the zero minute we repaint all the black squares to the 0 color. During the i -th minute we repaint to the i color the initially black squares that have exactly four corner-adjacent squares painted i ΓÇë-ΓÇë1 (all such squares are repainted simultaneously). This process continues ad infinitum. You have to figure out how many squares we repainted exactly x times.

The upper left square of the board has to be assumed to be always black. Two squares are called corner-adjacent, if they have exactly one common point.

## Input

The first line contains integers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë5000 ). The second line contains integer x ( 1ΓÇëΓëñΓÇë x ΓÇëΓëñΓÇë10 9 ).

## Output

Print how many squares will be painted exactly x times.

## Examples

Example 1:
```
3 3
1
```
```
4
```
