# E. Race

**Submission:** https://codeforces.com/contest/43/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Today s kilometer long auto race takes place in Berland. The track is represented by a straight line as long as s kilometers. There are n cars taking part in the race, all of them start simultaneously at the very beginning of the track. For every car is known its behavior ΓÇö the system of segments on each of which the speed of the car is constant. The j -th segment of the i -th car is pair ( v i ,ΓÇë j ,ΓÇë t i ,ΓÇë j ) , where v i ,ΓÇë j is the car's speed on the whole segment in kilometers per hour and t i ,ΓÇë j is for how many hours the car had been driving at that speed. The segments are given in the order in which they are "being driven on" by the cars.

Your task is to find out how many times during the race some car managed to have a lead over another car. A lead is considered a situation when one car appears in front of another car. It is known, that all the leads happen instantly, i. e. there are no such time segment of positive length, during which some two cars drive "together". At one moment of time on one and the same point several leads may appear. In this case all of them should be taken individually. Meetings of cars at the start and finish are not considered to be counted as leads.

## Input

The first line contains two integers n and s ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100,ΓÇë1ΓÇëΓëñΓÇë s ΓÇëΓëñΓÇë10 6 ) ΓÇö the number of cars and the length of the track in kilometers. Then follow n lines ΓÇö the description of the system of segments for each car. Every description starts with integer k ( 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë100 ) ΓÇö the number of segments in the system. Then k space-separated pairs of integers are written. Each pair is the speed and time of the segment. These integers are positive and don't exceed 1000. It is guaranteed, that the sum of lengths of all segments (in kilometers) for each car equals to s ; and all the leads happen instantly.

## Output

Print the single number ΓÇö the number of times some car managed to take the lead over another car during the race.

## Examples

Example 1:
```
2 33
2 5 1 2 14
1 3 11
```
```
1
```
