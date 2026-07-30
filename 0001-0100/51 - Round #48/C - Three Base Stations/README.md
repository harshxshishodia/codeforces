# C. Three Base Stations

**Submission:** https://codeforces.com/contest/51/problem/C

**Limits:** 1 second / 256 megabytes

## Problem Statement

The New Vasjuki village is stretched along the motorway and that's why every house on it is characterized by its shift relative to some fixed point ΓÇö the x i coordinate. The village consists of n houses, the i -th house is located in the point with coordinates of x i .

TELE3, a cellular communication provider planned to locate three base stations so as to provide every house in the village with cellular communication. The base station having power d located in the point t provides with communication all the houses on the segment [ t ΓÇë-ΓÇë d ,ΓÇë t ΓÇë+ΓÇë d ] (including boundaries).

To simplify the integration (and simply not to mix anything up) all the three stations are planned to possess the equal power of d . Which minimal value of d is enough to provide all the houses in the village with cellular communication.

## Input

The first line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë2┬╖10 5 ) which represents the number of houses in the village. The second line contains the coordinates of houses ΓÇö the sequence x 1 ,ΓÇë x 2 ,ΓÇë...,ΓÇë x n of integer numbers ( 1ΓÇëΓëñΓÇë x i ΓÇëΓëñΓÇë10 9 ). It is possible that two or more houses are located on one point. The coordinates are given in a arbitrary order.

## Output

Print the required minimal power d . In the second line print three numbers ΓÇö the possible coordinates of the base stations' location. Print the coordinates with 6 digits after the decimal point. The positions of the stations can be any from 0 to 2┬╖10 9 inclusively. It is accepted for the base stations to have matching coordinates. If there are many solutions, print any of them.

## Examples

Example 1:
```
4
1 2 3 4
```
```
0.500000
1.500000 2.500000 3.500000
```
