# F. Oil

**Submission:** https://codeforces.com/contest/72/problem/F

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

After the nationalization of the oil industry, Dr. Mosaddegh wants to dig some oil wells to extract all the oil in Persian Gulf. But Persian Gulf is huge and has an infinite amount of oil. So Dr. Mosaddegh works only on a rectangular plane of size n ΓÇë├ùΓÇë m of the Persian Gulf. Each of the cells in this rectangle either contains an infinite amount of oil or nothing.

Two cells are considered adjacent if and only if they have a common edge, a path is a sequence c 1 ,ΓÇë c 2 ,ΓÇë...,ΓÇë c x of cells so that all of them contain oil and for each i , c i is adjacent to c i ΓÇë-ΓÇë1 and c i ΓÇë+ΓÇë1 (if they exist). Two cells are considered connected to each other if and only if there exists a path between them. If we dig a well in a certain cell, we can extract oil from all the cells that are connected to it by oil paths. It is not allowed to dig wells on empty cells.

Dr. Mosaddegh also knows that in Persian Gulf, the empty cells form rows and columns. I. e. if some cell is empty, then it's column is completely empty or it's row is completely empty, or both.

Help Dr. Mosaddegh find out how many wells he has to dig to access all the oil in that region.

## Input

In the first line there are two positive integers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë100 ).

In the second line there is an integer t ( 0ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë n ), the number of empty rows. t distinct positive integers follow, these are the numbers of empty rows and are in range [1,ΓÇë n ] .

In the second line there is an integer s ( 0ΓÇëΓëñΓÇë s ΓÇëΓëñΓÇë m ) that shows the number of columns not having any oil. s distinct positive integers follow, these are the numbers of empty columns and are in range of [1,ΓÇë m ] .

Note that rows are numbered from 1 to n (from top to bottom) and columns are numbered from 1 to m (from left to right).

## Output

A single integer, the minimum number of wells that Dr. Mossadegh has to dig.

This is actually finding how many regions are made by removing the given rows and columns.

## Examples

Example 1:
```
2 3
1 2
1 2
```
```
2
```
