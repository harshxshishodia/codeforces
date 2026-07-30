# B. Game of chess unfinished

**Submission:** https://codeforces.com/contest/42/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Once Volodya was at the museum and saw a regular chessboard as a museum piece. And there were only four chess pieces on it: two white rooks, a white king and a black king. "Aha, blacks certainly didn't win!", ΓÇö Volodya said and was right for sure. And your task is to say whether whites had won or not.

Pieces on the chessboard are guaranteed to represent a correct position (every piece occupies one cell, no two pieces occupy the same cell and kings cannot take each other). Thus, your task is only to decide whether whites mate blacks. We would remind you that it means that the black king can be taken by one of the opponent's pieces at the moment and also it cannot move to an unbeaten position. A rook moves vertically or horizontally by any number of free cells (assuming there are no other pieces on its path), a king ΓÇö to the adjacent cells (either by corner or by side). Certainly, pieces cannot leave the board. The black king might be able to take opponent's rooks at his turn (see sample 3).

## Input

The input contains 4 space-separated piece positions: positions of the two rooks, the white king and the black king. Each position on 8ΓÇë├ùΓÇë8 chessboard is denoted by two symbols ΓÇö ( 'a' - 'h' ) and ( '1' - '8' ) ΓÇö which stand for horizontal and vertical coordinates of the cell occupied by the piece. It is guaranteed, that no two pieces occupy the same cell, and kings cannot take each other.

## Output

Output should contain one word: "CHECKMATE" if whites mate blacks, and "OTHER" otherwise.

## Examples

Example 1:
```
a6 b4 c8 a8
```
```
CHECKMATE
```
