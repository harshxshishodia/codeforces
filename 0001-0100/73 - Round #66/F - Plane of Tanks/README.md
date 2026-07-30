# F. Plane of Tanks

**Submission:** https://codeforces.com/contest/73/problem/F

**Limits:** 4 seconds / 256 megabytes

## Problem Statement

Vasya plays the Plane of Tanks. The tanks in this game keep trying to finish each other off. But your "Pedalny" is not like that... He just needs to drive in a straight line from point A to point B on the plane. Unfortunately, on the same plane are n enemy tanks. We shall regard all the tanks as points. At the initial moment of time Pedalny is at the point A . Enemy tanks would be happy to destroy it immediately, but initially their turrets are tuned in other directions. Specifically, for each tank we know the initial rotation of the turret a i (the angle in radians relative to the OX axis in the counterclockwise direction) and the maximum speed of rotation of the turret w i (radians per second). If at any point of time a tank turret will be aimed precisely at the tank Pedalny, then the enemy fires and it never misses. Pedalny can endure no more than k shots. Gun reloading takes very much time, so we can assume that every enemy will produce no more than one shot. Your task is to determine what minimum speed of v Pedalny must have to get to the point B . It is believed that Pedalny is able to instantly develop the speed of v , and the first k shots at him do not reduce the speed and do not change the coordinates of the tank.

## Input

The first line contains 4 numbers ΓÇô the coordinates of points A and B (in meters), the points do not coincide. On the second line number n is given ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 4 ). It is the number of enemy tanks. Each of the following n lines contain the coordinates of a corresponding tank x i ,ΓÇë y i and its parameters a i and w i ( 0ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë2╧Ç , 0ΓÇëΓëñΓÇë w i ΓÇëΓëñΓÇë100 ). Numbers a i and w i contain at most 5 digits after the decimal point. All coordinates are integers and their absolute values do not exceed 10 5 . Enemy tanks can rotate a turret in the clockwise as well as in the counterclockwise direction at the angular speed of not more than w i . It is guaranteed that each of the enemy tanks will need at least 0.1 seconds to aim at any point of the segment AB and each of the enemy tanks is posistioned no closer than 0.1 meters to line AB . On the last line is given the number k ( 0ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë n ).

## Output

Print a single number with absolute or relative error no more than 10 ΓÇë-ΓÇë4 ΓÇö the minimum required speed of Pedalny in meters per second.

## Examples

Example 1:
```
0 0 10 0
1
5 -5 4.71238 1
0
```
```
4.2441
```
