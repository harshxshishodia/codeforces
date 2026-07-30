# D. Roads not only in Berland

**Submission:** https://codeforces.com/contest/25/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Berland Government decided to improve relations with neighboring countries. First of all, it was decided to build new roads so that from each city of Berland and neighboring countries it became possible to reach all the others. There are n cities in Berland and neighboring countries in total and exactly n ΓÇë-ΓÇë1 two-way roads. Because of the recent financial crisis, the Berland Government is strongly pressed for money, so to build a new road it has to close some of the existing ones. Every day it is possible to close one existing road and immediately build a new one. Your task is to determine how many days would be needed to rebuild roads so that from each city it became possible to reach all the others, and to draw a plan of closure of old roads and building of new ones.

## Input

The first line contains integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) ΓÇö amount of cities in Berland and neighboring countries. Next n ΓÇë-ΓÇë1 lines contain the description of roads. Each road is described by two space-separated integers a i , b i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë a i ΓÇëΓëáΓÇë b i ) ΓÇö pair of cities, which the road connects. It can't be more than one road between a pair of cities. No road connects the city with itself.

## Output

Output the answer, number t ΓÇö what is the least amount of days needed to rebuild roads so that from each city it became possible to reach all the others. Then output t lines ΓÇö the plan of closure of old roads and building of new ones. Each line should describe one day in the format i j u v ΓÇö it means that road between cities i and j became closed and a new road between cities u and v is built. Cities are numbered from 1. If the answer is not unique, output any.

## Examples

Example 1:
```
2
1 2
```
```
0
```
