# C. Lucky Tickets

**Submission:** https://codeforces.com/contest/70/problem/C

**Limits:** 1.5 seconds / 256 megabytes

## Problem Statement

In Walrusland public transport tickets are characterized by two integers: by the number of the series and by the number of the ticket in the series. Let the series number be represented by a and the ticket number ΓÇö by b , then a ticket is described by the ordered pair of numbers ( a ,ΓÇë b ) . 

The walruses believe that a ticket is lucky if a ΓÇë*ΓÇë b ΓÇë=ΓÇë rev ( a )ΓÇë*ΓÇë rev ( b ) . The function rev ( x ) reverses a number written in the decimal system, at that the leading zeroes disappear. For example, rev (12343)ΓÇë=ΓÇë34321 , rev (1200)ΓÇë=ΓÇë21 .

The Public Transport Management Committee wants to release x series, each containing y tickets, so that at least w lucky tickets were released and the total number of released tickets ( x ΓÇë*ΓÇë y ) were minimum. The series are numbered from 1 to x inclusive. The tickets in each series are numbered from 1 to y inclusive. The Transport Committee cannot release more than max x series and more than max y tickets in one series.

## Input

The first line contains three integers max x , max y , w ( 1ΓÇëΓëñΓÇë max x ,ΓÇë max y ΓÇëΓëñΓÇë10 5 , 1ΓÇëΓëñΓÇë w ΓÇëΓëñΓÇë10 7 ).

## Output

Print on a single line two space-separated numbers, the x and the y . If there are several possible variants, print any of them. If such x and y do not exist, print a single number ΓÇë-ΓÇë1 .

## Examples

Example 1:
```
2 2 1
```
```
1 1
```
