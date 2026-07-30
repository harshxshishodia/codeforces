# A. Power Consumption Calculation

**Submission:** https://codeforces.com/contest/10/problem/A

**Limits:** 1 second / 256 megabytes

## Problem Statement

Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P 1 watt per minute. T 1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P 2 watt per minute. Finally, after T 2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P 3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [ l 1 ,ΓÇë r 1 ],ΓÇë[ l 2 ,ΓÇë r 2 ],ΓÇë...,ΓÇë[ l n ,ΓÇë r n ] . During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [ l 1 ,ΓÇë r n ] .

## Input

The first line contains 6 integer numbers n , P 1 , P 2 , P 3 , T 1 , T 2 ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100,ΓÇë0ΓÇëΓëñΓÇë P 1 ,ΓÇë P 2 ,ΓÇë P 3 ΓÇëΓëñΓÇë100,ΓÇë1ΓÇëΓëñΓÇë T 1 ,ΓÇë T 2 ΓÇëΓëñΓÇë60 ). The following n lines contain description of Tom's work. Each i -th of these lines contains two space-separated integers l i and r i ( 0ΓÇëΓëñΓÇë l i ΓÇë<ΓÇë r i ΓÇëΓëñΓÇë1440 , r i ΓÇë<ΓÇë l i ΓÇë+ΓÇë1 for i ΓÇë<ΓÇë n ), which stand for the start and the end of the i -th period of work.

## Output

Output the answer to the problem.

## Examples

Example 1:
```
1 3 2 1 5 10
0 10
```
```
30
```
