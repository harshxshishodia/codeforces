# A. Reflection

**Submission:** https://codeforces.com/contest/86/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

For each positive integer n consider the integer ╧ê( n ) which is obtained from n by replacing every digit a in the decimal notation of n with the digit (9ΓÇëΓÇë-ΓÇëΓÇë a ) . We say that ╧ê( n ) is the reflection of n . For example, reflection of 192 equals 807 . Note that leading zeros (if any) should be omitted. So reflection of 9 equals 0 , reflection of 91 equals 8 .

Let us call the weight of the number the product of the number and its reflection. Thus, the weight of the number 10 is equal to 10┬╖89ΓÇë=ΓÇë890 .

Your task is to find the maximum weight of the numbers in the given range [ l ,ΓÇë r ] (boundaries are included).

## Input

Input contains two space-separated integers l and r ( 1ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë r ΓÇëΓëñΓÇë10 9 ) ΓÇö bounds of the range.

## Output

Output should contain single integer number: maximum value of the product n ┬╖╧ê( n ) , where l ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë r .

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout (also you may use %I64d ).

## Examples

Example 1:
```
3 7
```
```
20
```

## Note

In the third sample weight of 8 equals 8┬╖1ΓÇë=ΓÇë8 , weight of 9 equals 9┬╖0ΓÇë=ΓÇë0 , weight of 10 equals 890 .

Thus, maximum value of the product is equal to 890 .
