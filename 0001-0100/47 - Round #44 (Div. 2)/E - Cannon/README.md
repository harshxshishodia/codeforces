# E. Cannon

**Submission:** https://codeforces.com/contest/47/problem/E

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

Bertown is under siege! The attackers have blocked all the ways out and their cannon is bombarding the city. Fortunately, Berland intelligence managed to intercept the enemies' shooting plan. Let's introduce the Cartesian system of coordinates, the origin of which coincides with the cannon's position, the Ox axis is directed rightwards in the city's direction, the Oy axis is directed upwards (to the sky). The cannon will make n more shots. The cannon balls' initial speeds are the same in all the shots and are equal to V , so that every shot is characterized by only one number alpha i which represents the angle at which the cannon fires. Due to the cannon's technical peculiarities this angle does not exceed 45 angles ( ╧ÇΓÇë/ΓÇë4 ). We disregard the cannon sizes and consider the firing made from the point (0,ΓÇë0) .

The balls fly according to the known physical laws of a body thrown towards the horizon at an angle: 
 v x ( t )ΓÇë=ΓÇë V ┬╖ cos ( alpha ) v y ( t )ΓÇë=ΓÇë V ┬╖ sin ( alpha )┬áΓÇëΓÇôΓÇë┬á g ┬╖ t x ( t )ΓÇë=ΓÇë V ┬╖ cos ( alpha )┬╖ t y ( t )ΓÇë=ΓÇë V ┬╖ sin ( alpha )┬╖ t ┬áΓÇëΓÇôΓÇë┬á g ┬╖ t 2 ΓÇë/ΓÇë2 
Think of the acceleration of gravity g as equal to 9.8 .

Bertown defends m walls. The i -th wall is represented as a vertical segment ( x i ,ΓÇë0)ΓÇë-ΓÇë( x i ,ΓÇë y i ) . When a ball hits a wall, it gets stuck in it and doesn't fly on. If a ball doesn't hit any wall it falls on the ground ( y ΓÇë=ΓÇë0 ) and stops. If the ball exactly hits the point ( x i ,ΓÇë y i ) , it is considered stuck. 

Your task is to find for each ball the coordinates of the point where it will be located in the end.

## Input

The first line contains integers n and V ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 4 ,ΓÇë1ΓÇëΓëñΓÇë V ΓÇëΓëñΓÇë1000 ) which represent the number of shots and the initial speed of every ball. The second line contains n space-separated real numbers alpha i ( 0ΓÇë<ΓÇë alpha i ΓÇë<ΓÇë╧ÇΓÇë/ΓÇë4 ) which represent the angles in radians at which the cannon will fire. The third line contains integer m ( 1ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10 5 ) which represents the number of walls. Then follow m lines, each containing two real numbers x i and y i ( 1ΓÇëΓëñΓÇë x i ΓÇëΓëñΓÇë1000,ΓÇë0ΓÇëΓëñΓÇë y i ΓÇëΓëñΓÇë1000 ) which represent the wallΓÇÖs coordinates. All the real numbers have no more than 4 decimal digits. The walls may partially overlap or even coincide.

## Output

Print n lines containing two real numbers each ΓÇö calculate for every ball the coordinates of its landing point. Your answer should have the relative or absolute error less than 10 ΓÇë-ΓÇë4 .

## Examples

Example 1:
```
2 10
0.7853
0.3
3
5.0 5.0
4.0 2.4
6.0 1.9
```
```
5.000000000 2.549499369
4.000000000 0.378324889
```
