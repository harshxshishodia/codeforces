# A. Guilty ΓÇö to the kitchen!

**Submission:** https://codeforces.com/contest/42/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

It's a very unfortunate day for Volodya today. He got bad mark in algebra and was therefore forced to do some work in the kitchen, namely to cook borscht (traditional Russian soup). This should also improve his algebra skills.

According to the borscht recipe it consists of n ingredients that have to be mixed in proportion litres (thus, there should be a 1 ΓÇë┬╖ x ,ΓÇë...,ΓÇë a n ΓÇë┬╖ x litres of corresponding ingredients mixed for some non-negative x ). In the kitchen Volodya found out that he has b 1 ,ΓÇë...,ΓÇë b n litres of these ingredients at his disposal correspondingly. In order to correct his algebra mistakes he ought to cook as much soup as possible in a V litres volume pan (which means the amount of soup cooked can be between 0 and V litres). What is the volume of borscht Volodya will cook ultimately?

## Input

The first line of the input contains two space-separated integers n and V ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë20,ΓÇë1ΓÇëΓëñΓÇë V ΓÇëΓëñΓÇë10000 ). The next line contains n space-separated integers a i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë100 ). Finally, the last line contains n space-separated integers b i ( 0ΓÇëΓëñΓÇë b i ΓÇëΓëñΓÇë100 ).

## Output

Your program should output just one real number ΓÇö the volume of soup that Volodya will cook. Your answer must have a relative or absolute error less than 10 ΓÇë-ΓÇë4 .

## Examples

Example 1:
```
1 100
1
40
```
```
40.0
```
