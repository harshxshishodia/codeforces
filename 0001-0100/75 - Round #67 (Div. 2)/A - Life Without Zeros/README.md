# A. Life Without Zeros

**Submission:** https://codeforces.com/contest/75/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Can you imagine our life if we removed all zeros from it? For sure we will have many problems.

In this problem we will have a simple example if we removed all zeros from our life, it's the addition operation. Let's assume you are given this equation a ΓÇë+ΓÇë b ΓÇë=ΓÇë c , where a and b are positive integers, and c is the sum of a and b . Now let's remove all zeros from this equation. Will the equation remain correct after removing all zeros?

For example if the equation is 101ΓÇë+ΓÇë102ΓÇë=ΓÇë203 , if we removed all zeros it will be 11ΓÇë+ΓÇë12ΓÇë=ΓÇë23 which is still a correct equation.

But if the equation is 105ΓÇë+ΓÇë106ΓÇë=ΓÇë211 , if we removed all zeros it will be 15ΓÇë+ΓÇë16ΓÇë=ΓÇë211 which is not a correct equation.

## Input

The input will consist of two lines, the first line will contain the integer a , and the second line will contain the integer b which are in the equation as described above ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ΓÇëΓëñΓÇë10 9 ). There won't be any leading zeros in both. The value of c should be calculated as c ΓÇë=ΓÇë a ΓÇë+ΓÇë b .

## Output

The output will be just one line, you should print " YES " if the equation will remain correct after removing all zeros, and print " NO " otherwise.

## Examples

Example 1:
```
101
102
```
```
YES
```
