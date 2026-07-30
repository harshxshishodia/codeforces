# D. Powerful array

**Submission:** https://codeforces.com/contest/86/problem/D

**Limits:** 5 seconds / 256 megabytes

## Problem Statement

An array of positive integers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n is given. Let us consider its arbitrary subarray a l ,ΓÇë a l ΓÇë+ΓÇë1 ...,ΓÇë a r , where 1ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë r ΓÇëΓëñΓÇë n . For every positive integer s denote by K s the number of occurrences of s into the subarray. We call the power of the subarray the sum of products K s ┬╖ K s ┬╖ s for every positive integer s . The sum contains only finite number of nonzero summands as the number of different values in the array is indeed finite.

You should calculate the power of t given subarrays.

## Input

First line contains two integers n and t ( 1ΓÇëΓëñΓÇë n ,ΓÇë t ΓÇëΓëñΓÇë200000 ) ΓÇö the array length and the number of queries correspondingly.

Second line contains n positive integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 6 ) ΓÇö the elements of the array.

Next t lines contain two positive integers l , r ( 1ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë r ΓÇëΓëñΓÇë n ) each ΓÇö the indices of the left and the right ends of the corresponding subarray.

## Output

Output t lines, the i -th line of the output should contain single positive integer ΓÇö the power of the i -th query subarray.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout stream (also you may use %I64d ).

## Examples

Example 1:
```
3 2
1 2 1
1 2
1 3
```
```
3
6
```

## Note

Consider the following array (see the second sample) and its [2, 7] subarray (elements of the subarray are colored): 
 Then K 1 ΓÇë=ΓÇë3 , K 2 ΓÇë=ΓÇë2 , K 3 ΓÇë=ΓÇë1 , so the power is equal to 3 2 ┬╖1ΓÇë+ΓÇë2 2 ┬╖2ΓÇë+ΓÇë1 2 ┬╖3ΓÇë=ΓÇë20 .
