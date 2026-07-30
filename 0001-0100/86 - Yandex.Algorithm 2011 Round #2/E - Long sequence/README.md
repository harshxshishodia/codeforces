# E. Long sequence

**Submission:** https://codeforces.com/contest/86/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

A sequence a 0 ,ΓÇë a 1 ,ΓÇë... is called a recurrent binary sequence , if each term a i ( i ΓÇë=ΓÇë0,ΓÇë1,ΓÇë...) is equal to 0 or 1 and there exist coefficients such that 
 a n ΓÇë=ΓÇë c 1 ┬╖ a n ΓÇë-ΓÇë1 ΓÇë+ΓÇë c 2 ┬╖ a n ΓÇë-ΓÇë2 ΓÇë+ΓÇë...ΓÇë+ΓÇë c k ┬╖ a n ΓÇë-ΓÇë k ( mod 2),ΓÇë for all n ΓÇëΓëÑΓÇë k . Assume that not all of c i are zeros.
Note that such a sequence can be uniquely recovered from any k -tuple { a s ,ΓÇë a s ΓÇë+ΓÇë1 ,ΓÇë...,ΓÇë a s ΓÇë+ΓÇë k ΓÇë-ΓÇë1 } and so it is periodic. Moreover, if a k -tuple contains only zeros, then the sequence contains only zeros, so this case is not very interesting. Otherwise the minimal period of the sequence is not greater than 2 k ΓÇë-ΓÇë1 , as k -tuple determines next element, and there are 2 k ΓÇë-ΓÇë1 non-zero k -tuples. Let us call a sequence long if its minimal period is exactly 2 k ΓÇë-ΓÇë1 . Your task is to find a long sequence for a given k , if there is any.

## Input

Input contains a single integer k ( 2ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë50 ).

## Output

If there is no long sequence for a given k , output "-1" (without quotes). Otherwise the first line of the output should contain k integer numbers: c 1 ,ΓÇë c 2 ,ΓÇë...,ΓÇë c k (coefficients). The second line should contain first k elements of the sequence: a 0 ,ΓÇë a 1 ,ΓÇë...,ΓÇë a k ΓÇë-ΓÇë1 . All of them (elements and coefficients) should be equal to 0 or 1, and at least one c i has to be equal to 1.

If there are several solutions, output any.

## Examples

Example 1:
```
2
```
```
1 1
1 0
```

## Note

1. In the first sample: c 1 ΓÇë=ΓÇë1 , c 2 ΓÇë=ΓÇë1 , so a n ΓÇë=ΓÇë a n ΓÇë-ΓÇë1 ΓÇë+ΓÇë a n ΓÇë-ΓÇë2 ( mod 2) . Thus the sequence will be:
 
so its period equals 3ΓÇë=ΓÇë2 2 ΓÇë-ΓÇë1 .

2. In the second sample: c 1 ΓÇë=ΓÇë0 , c 2 ΓÇë=ΓÇë1 , c 3 ΓÇë=ΓÇë1 , so a n ΓÇë=ΓÇë a n ΓÇë-ΓÇë2 ΓÇë+ΓÇë a n ΓÇë-ΓÇë3 ( mod 2) . Thus our sequence is:
 
and its period equals 7ΓÇë=ΓÇë2 3 ΓÇë-ΓÇë1 .

Periods are colored.
