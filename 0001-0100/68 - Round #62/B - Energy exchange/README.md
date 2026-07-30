# B. Energy exchange

**Submission:** https://codeforces.com/contest/68/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

It is well known that the planet suffers from the energy crisis. Little Petya doesn't like that and wants to save the world. For this purpose he needs every accumulator to contain the same amount of energy. Initially every accumulator has some amount of energy: the i -th accumulator has a i units of energy. Energy can be transferred from one accumulator to the other. Every time x units of energy are transferred ( x is not necessarily an integer) k percent of it is lost. That is, if x units were transferred from one accumulator to the other, amount of energy in the first one decreased by x units and in other increased by units.

Your task is to help Petya find what maximum equal amount of energy can be stored in each accumulator after the transfers.

## Input

First line of the input contains two integers n and k ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10000,ΓÇë0ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë99 ) ΓÇö number of accumulators and the percent of energy that is lost during transfers.

Next line contains n integers a 1 ,ΓÇë a 2 ,ΓÇë... ,ΓÇë a n ΓÇö amounts of energy in the first, second, .., n -th accumulator respectively ( 0ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë1000,ΓÇë1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ).

## Output

Output maximum possible amount of energy that can remain in each of accumulators after the transfers of energy.

The absolute or relative error in the answer should not exceed 10 ΓÇë-ΓÇë6 .

## Examples

Example 1:
```
3 50
4 2 1
```
```
2.000000000
```
