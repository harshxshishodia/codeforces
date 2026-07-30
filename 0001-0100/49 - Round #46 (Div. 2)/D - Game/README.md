# D. Game

**Submission:** https://codeforces.com/contest/49/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya and Petya have invented a new game. Vasya takes a stripe consisting of 1ΓÇë├ùΓÇë n square and paints the squares black and white. After that Petya can start moves ΓÇö during a move he may choose any two neighboring squares of one color and repaint these two squares any way he wants, perhaps in different colors. Petya can only repaint the squares in white and black colors. PetyaΓÇÖs aim is to repaint the stripe so that no two neighboring squares were of one color. Help Petya, using the given initial coloring, find the minimum number of moves Petya needs to win.

## Input

The first line contains number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) which represents the stripeΓÇÖs length. The second line contains exactly n symbols ΓÇö the lineΓÇÖs initial coloring. 0 corresponds to a white square, 1 corresponds to a black one.

## Output

If Petya cannot win with such an initial coloring, print -1 . Otherwise print the minimum number of moves Petya needs to win.

## Examples

Example 1:
```
6
111010
```
```
1
```

## Note

In the first sample Petya can take squares 1 and 2. He repaints square 1 to black and square 2 to white.

In the second sample Petya can take squares 2 and 3. He repaints square 2 to white and square 3 to black.
