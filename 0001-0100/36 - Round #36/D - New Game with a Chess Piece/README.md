# D. New Game with a Chess Piece

**Submission:** https://codeforces.com/contest/36/problem/D

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

Petya and Vasya are inventing a new game that requires a rectangular board and one chess piece. At the beginning of the game the piece stands in the upper-left corner of the board. Two players move the piece in turns. Each turn the chess piece can be moved either one square to the right or one square down or jump k squares diagonally down and to the right. The player who canΓÇÖt move the piece loses. 
 
The guys havenΓÇÖt yet thought what to call the game or the best size of the board for it. Your task is to write a program that can determine the outcome of the game depending on the board size.

## Input

The first input line contains two integers t and k ( 1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë20 , 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë10 9 ). Each of the following t lines contains two numbers n , m ΓÇö the boardΓÇÖs length and width ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë10 9 ).

## Output

Output t lines that can determine the outcomes of the game on every board. Write ┬½+┬╗ if the first player is a winner, and ┬½-┬╗ otherwise.

## Examples

Example 1:
```
10 2
1 1
1 2
2 1
2 2
1 3
2 3
3 1
3 2
3 3
4 3
```
```
-
+
+
-
-
+
-
+
+
+
```
