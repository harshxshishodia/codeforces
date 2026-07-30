# D. Solitaire

**Submission:** https://codeforces.com/contest/71/problem/D

**Limits:** 1.5 seconds / 256 megabytes

## Problem Statement

Vasya has a pack of 54 cards ( 52 standard cards and 2 distinct jokers). That is all he has at the moment. Not to die from boredom, Vasya plays Solitaire with them.

Vasya lays out nm cards as a rectangle n ΓÇë├ùΓÇë m . If there are jokers among them, then Vasya should change them with some of the rest of 54ΓÇë-ΓÇë nm cards (which are not layed out) so that there were no jokers left. Vasya can pick the cards to replace the jokers arbitrarily. Remember, that each card presents in pack exactly once (i. e. in a single copy ). Vasya tries to perform the replacements so that the solitaire was solved .

Vasya thinks that the solitaire is solved if after the jokers are replaced, there exist two non-overlapping squares 3ΓÇë├ùΓÇë3 , inside each of which all the cards either have the same suit, or pairwise different ranks.

Determine by the initial position whether the solitaire can be solved or not. If it can be solved, show the way in which it is possible.

## Input

The first line contains integers n and m ( 3ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë17 , n ΓÇë├ùΓÇë m ΓÇëΓëñΓÇë52 ). Next n lines contain m words each. Each word consists of two letters. The jokers are defined as " J1 " and " J2 " correspondingly. For the rest of the cards, the first letter stands for the rank and the second one ΓÇö for the suit. The possible ranks are: " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " T ", " J ", " Q ", " K " and " A ". The possible suits are: " C ", " D ", " H " and " S ". All the cards are different.

## Output

If the Solitaire can be solved, print on the first line " Solution exists. " without the quotes. On the second line print in what way the jokers can be replaced. Three variants are possible:

 
- " There are no jokers. ", if there are no jokers in the input data.
- " Replace J x with y . ", if there is one joker. x is its number, and y is the card it should be replaced with.
- " Replace J1 with x and J2 with y . ", if both jokers are present in the input data. x and y here represent distinct cards with which one should replace the first and the second jokers correspondingly.

On the third line print the coordinates of the upper left corner of the first square 3ΓÇë├ùΓÇë3 in the format " Put the first square to ( r , c ). ", where r and c are the row and the column correspondingly. In the same manner print on the fourth line the coordinates of the second square 3ΓÇë├ùΓÇë3 in the format " Put the second square to ( r , c ). ".

If there are several solutions to that problem, print any of them.

If there are no solutions, print of the single line " No solution. " without the quotes.

See the samples to understand the output format better.

## Examples

Example 1:
```
4 6
2S 3S 4S 7S 8S AS
5H 6H 7H 5S TC AC
8H 9H TH 7C 8C 9C
2D 2C 3C 4C 5C 6C
```
```
No solution.
```

## Note

The pretests cover all the possible output formats.
