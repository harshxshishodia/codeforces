# E. Security System

**Submission:** https://codeforces.com/contest/79/problem/E

**Limits:** 1 second / 256 megabytes

## Problem Statement

Fox Ciel safely returned to her castle, but there was something wrong with the security system of the castle: sensors attached in the castle were covering her.

Ciel is at point (1,ΓÇë1) of the castle now, and wants to move to point ( n ,ΓÇë n ) , which is the position of her room. By one step, Ciel can move from point ( x ,ΓÇë y ) to either ( x ΓÇë+ΓÇë1,ΓÇë y ) (rightward) or ( x ,ΓÇë y ΓÇë+ΓÇë1) (upward).

In her castle, c 2 sensors are set at points ( a ΓÇë+ΓÇë i ,ΓÇë b ΓÇë+ΓÇë j ) (for every integer i and j such that: 0ΓÇëΓëñΓÇë i ΓÇë<ΓÇë c ,ΓÇë0ΓÇëΓëñΓÇë j ΓÇë<ΓÇë c ).

Each sensor has a count value and decreases its count value every time Ciel moves. Initially, the count value of each sensor is t . Every time Ciel moves to point ( x ,ΓÇë y ) , the count value of a sensor at point ( u ,ΓÇë v ) decreases by ( | u ΓÇë-ΓÇë x |ΓÇë+ΓÇë| v ΓÇë-ΓÇë y | ). When the count value of some sensor becomes strictly less than 0 , the sensor will catch Ciel as a suspicious individual!

Determine whether Ciel can move from (1,ΓÇë1) to ( n ,ΓÇë n ) without being caught by a sensor, and if it is possible, output her steps. Assume that Ciel can move to every point even if there is a censor on the point.

## Input

In the first line there are five integers n ,ΓÇë t ,ΓÇë a ,ΓÇë b ,ΓÇë c ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë2┬╖10 5 ,ΓÇë 0ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë10 14 ,ΓÇë 1ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë n ΓÇë-ΓÇë c ΓÇë+ΓÇë1,ΓÇë 1ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë n ΓÇë-ΓÇë c ΓÇë+ΓÇë1,ΓÇë 1ΓÇëΓëñΓÇë c ΓÇëΓëñΓÇë n ).

Please do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin stream (also you may use the %I64d specificator).

## Output

If Ciel's objective is possible, output in first line 2 n ΓÇë-ΓÇë2 characters that represent her feasible steps, where i -th character is R if i -th step is moving rightward, or U if moving upward. If there are several solution, output lexicographically first one. Character R is lexicographically earlier than the character U .

If her objective is impossible, output Impossible .

## Examples

Example 1:
```
5 25 2 4 1
```
```
RRUURURU
```

## Note

The answers for the first sample and the second sample are shown on the picture: 
 Here, a red point represents a point that contains a sensor.
