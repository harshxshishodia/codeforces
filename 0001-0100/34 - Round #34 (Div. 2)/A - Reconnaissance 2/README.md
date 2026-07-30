# A. Reconnaissance 2

**Submission:** https://codeforces.com/contest/34/problem/A

**Limits:** 1 second / 256 megabytes

## Problem Statement

n soldiers stand in a circle. For each soldier, his height a i is known. A reconnaissance unit can be made of such two neighbouring soldiers, whose height difference is minimal, i.e. | a i ΓÇë-ΓÇë a j | is minimal. So each of them will be less noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

## Input

The first line contains an integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the number of soldiers. Then follow the heights of the soldiers in their order in the circle ΓÇö n space-separated integers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë1000 ). The soldier heights are given in a clockwise or counterclockwise direction.

## Output

Output two integers ΓÇö indices of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimal solutions, output any of them. Remember that the soldiers stand in a circle.

## Examples

Example 1:
```
5
10 12 13 15 10
```
```
5 1
```
