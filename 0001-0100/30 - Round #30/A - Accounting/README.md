# A. Accounting

**Submission:** https://codeforces.com/contest/30/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

A long time ago in some far country lived king Copa. After the recent king's reform, he got so large powers that started to keep the books by himself.

The total income A of his kingdom during 0 -th year is known, as well as the total income B during n -th year (these numbers can be negative ΓÇö it means that there was a loss in the correspondent year). 

King wants to show financial stability. To do this, he needs to find common coefficient X ΓÇö the coefficient of income growth during one year. This coefficient should satisfy the equation:
 A ┬╖ X n ΓÇë=ΓÇë B . 
Surely, the king is not going to do this job by himself, and demands you to find such number X .

It is necessary to point out that the fractional numbers are not used in kingdom's economy. That's why all input numbers as well as coefficient X must be integers. The number X may be zero or negative.

## Input

The input contains three integers A , B , n ( | A |,ΓÇë| B |ΓÇëΓëñΓÇë1000 , 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 ).

## Output

Output the required integer coefficient X , or ┬½No solution┬╗, if such a coefficient does not exist or it is fractional. If there are several possible solutions, output any of them.

## Examples

Example 1:
```
2 18 2
```
```
3
```
