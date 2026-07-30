# E. Enemy is weak

**Submission:** https://codeforces.com/contest/61/problem/E

**Limits:** 5 seconds / 256 megabytes

## Problem Statement

The Romans have attacked again. This time they are much more than the Persians but Shapur is ready to defeat them. He says: "A lion is never afraid of a hundred sheep". 

Nevertheless Shapur has to find weaknesses in the Roman army to defeat them. So he gives the army a weakness number.

In Shapur's opinion the weakness of an army is equal to the number of triplets i ,ΓÇë j ,ΓÇë k such that i ΓÇë<ΓÇë j ΓÇë<ΓÇë k and a i ΓÇë>ΓÇë a j ΓÇë>ΓÇë a k where a x is the power of man standing at position x . The Roman army has one special trait ΓÇö powers of all the people in it are distinct.

Help Shapur find out how weak the Romans are.

## Input

The first line of input contains a single number n ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 6 ) ΓÇö the number of men in Roman army. Next line contains n different positive integers a i ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ) ΓÇö powers of men in the Roman army.

## Output

A single integer number, the weakness of the Roman army. 

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d ).

## Examples

Example 1:
```
3
3 2 1
```
```
1
```
