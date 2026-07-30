# C. Industrial Nim

**Submission:** https://codeforces.com/contest/15/problem/C

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

There are n stone quarries in Petrograd.

Each quarry owns m i dumpers ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ). It is known that the first dumper of the i -th quarry has x i stones in it, the second dumper has x i ΓÇë+ΓÇë1 stones in it, the third has x i ΓÇë+ΓÇë2 , and the m i -th dumper (the last for the i -th quarry) has x i ΓÇë+ΓÇë m i ΓÇë-ΓÇë1 stones in it.

Two oligarchs play a well-known game Nim. Players take turns removing stones from dumpers. On each turn, a player can select any dumper and remove any non-zero amount of stones from it. The player who cannot take a stone loses.

Your task is to find out which oligarch will win, provided that both of them play optimally. The oligarchs asked you not to reveal their names. So, let's call the one who takes the first stone ┬½ tolik ┬╗ and the other one ┬½ bolik ┬╗.

## Input

The first line of the input contains one integer number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö the amount of quarries. Then there follow n lines, each of them contains two space-separated integers x i and m i ( 1ΓÇëΓëñΓÇë x i ,ΓÇë m i ΓÇëΓëñΓÇë10 16 ) ΓÇö the amount of stones in the first dumper of the i -th quarry and the number of dumpers at the i -th quarry.

## Output

Output ┬½ tolik ┬╗ if the oligarch who takes a stone first wins, and ┬½ bolik ┬╗ otherwise.

## Examples

Example 1:
```
2
2 1
3 2
```
```
tolik
```
