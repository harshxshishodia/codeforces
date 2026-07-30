# A. Letter

**Submission:** https://codeforces.com/contest/14/problem/A

**Limits:** 1 second / 64 megabytes

## Problem Statement

A boy Bob likes to draw. Not long ago he bought a rectangular graph (checked) sheet with n rows and m columns. Bob shaded some of the squares on the sheet. Having seen his masterpiece, he decided to share it with his elder brother, who lives in Flatland. Now Bob has to send his picture by post, but because of the world economic crisis and high oil prices, he wants to send his creation, but to spend as little money as possible. For each sent square of paper (no matter whether it is shaded or not) Bob has to pay 3.14 burles. Please, help Bob cut out of his masterpiece a rectangle of the minimum cost, that will contain all the shaded squares. The rectangle's sides should be parallel to the sheet's sides.

## Input

The first line of the input data contains numbers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë50 ), n ΓÇö amount of lines, and m ΓÇö amount of columns on Bob's sheet. The following n lines contain m characters each. Character ┬½ . ┬╗ stands for a non-shaded square on the sheet, and ┬½ * ┬╗ ΓÇö for a shaded square. It is guaranteed that Bob has shaded at least one square.

## Output

Output the required rectangle of the minimum cost. Study the output data in the sample tests to understand the output format better.

## Examples

Example 1:
```
6 7
.......
..***..
..*....
..***..
..*....
..***..
```
```
***
*..
***
*..
***
```
