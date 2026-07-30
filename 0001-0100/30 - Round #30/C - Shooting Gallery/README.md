# C. Shooting Gallery

**Submission:** https://codeforces.com/contest/30/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One warm and sunny day king Copa decided to visit the shooting gallery, located at the Central Park, and try to win the main prize ΓÇö big pink plush panda. The king is not good at shooting, so he invited you to help him.

The shooting gallery is an infinite vertical plane with Cartesian coordinate system on it. The targets are points on this plane. Each target is described by it's coordinates x i , and y i , by the time of it's appearance t i and by the number p i , which gives the probability that Copa hits this target if he aims at it.

A target appears and disappears instantly, so Copa can hit the target only if at the moment t i his gun sight aimed at ( x i ,ΓÇë y i ) . Speed of movement of the gun sight on the plane is equal to 1. Copa knows all the information about the targets beforehand (remember, he is a king!). He wants to play in the optimal way, which maximizes the expected value of the amount of hit targets. He can aim at any target at the moment 0.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ) ΓÇö amount of targets in the shooting gallery. Then n lines follow, each describing one target. Each description consists of four numbers x i , y i , t i , p i (where x i , y i , t i ΓÇö integers, ΓÇë-ΓÇë1000ΓÇëΓëñΓÇë x i ,ΓÇë y i ΓÇëΓëñΓÇë1000,ΓÇë0ΓÇëΓëñΓÇë t i ΓÇëΓëñΓÇë10 9 , real number p i is given with no more than 6 digits after the decimal point, 0ΓÇëΓëñΓÇë p i ΓÇëΓëñΓÇë1 ). No two targets may be at the same point.

## Output

Output the maximum expected value of the amount of targets that was shot by the king. Your answer will be accepted if it differs from the correct answer by not more than 10 ΓÇë-ΓÇë6 .

## Examples

Example 1:
```
1
0 0 0 0.5
```
```
0.5000000000
```
