# E. 3-cycles

**Submission:** https://codeforces.com/contest/41/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

During a recent research Berland scientists found out that there were n cities in Ancient Berland, joined by two-way paths. Any two cities are joined by no more than one path. No path joins a city with itself. According to a well-known tradition, the road network was built so that it would be impossible to choose three cities from each of which one can get to any other one directly. That is, there was no cycle exactly as long as 3. Unfortunately, the road map has not been preserved till nowadays. Now the scientists are interested how much developed a country Ancient Berland was. Help them - find, what maximal number of roads could be in the country. You also have to restore any of the possible road maps.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the number of cities in Berland.

## Output

On the first line must be printed number m ΓÇö the maximal number of roads in Berland. Then print m lines containing two numbers each ΓÇö the numbers of cities that the given road joins. The cities are numbered with integers from 1 to n . If there are several variants of solving the problem, print any of them.

## Examples

Example 1:
```
3
```
```
2
1 2
2 3
```
