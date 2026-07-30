# E. TV Game

**Submission:** https://codeforces.com/contest/31/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There is a new TV game on BerTV. In this game two players get a number A consisting of 2 n digits. Before each turn players determine who will make the next move. Each player should make exactly n moves. On it's turn i -th player takes the leftmost digit of A and appends it to his or her number S i . After that this leftmost digit is erased from A . Initially the numbers of both players ( S 1 and S 2 ) are ┬½empty┬╗. Leading zeroes in numbers A ,ΓÇë S 1 ,ΓÇë S 2 are allowed. In the end of the game the first player gets S 1 dollars, and the second gets S 2 dollars.

One day Homer and Marge came to play the game. They managed to know the number A beforehand. They want to find such sequence of their moves that both of them makes exactly n moves and which maximizes their total prize. Help them.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë18 ). The second line contains integer A consisting of exactly 2 n digits. This number can have leading zeroes.

## Output

Output the line of 2 n characters ┬½H┬╗ and ┬½M┬╗ ΓÇö the sequence of moves of Homer and Marge, which gives them maximum possible total prize. Each player must make exactly n moves. If there are several solutions, output any of them.

## Examples

Example 1:
```
2
1234
```
```
HHMM
```
