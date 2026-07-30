# E. Berland collider

**Submission:** https://codeforces.com/contest/24/problem/E

**Limits:** 1.5 seconds / 256 megabytes

## Problem Statement

Recently the construction of Berland collider has been completed. Collider can be represented as a long narrow tunnel that contains n particles. We associate with collider 1-dimensional coordinate system, going from left to right. For each particle we know its coordinate and velocity at the moment of start of the collider. The velocities of the particles don't change after the launch of the collider. Berland scientists think that the big bang will happen at the first collision of particles, whose velocities differs in directions. Help them to determine how much time elapses after the launch of the collider before the big bang happens.

## Input

The first line contains single integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë5┬╖10 5 ) ΓÇö amount of particles in the collider. Next n lines contain description of particles. Each particle is described by two integers x i , v i ( ΓÇë-ΓÇë10 9 ΓÇëΓëñΓÇë x i ,ΓÇë v i ΓÇëΓëñΓÇë10 9 ,ΓÇë v i ΓÇëΓëáΓÇë0 ) ΓÇö coordinate and velocity respectively. All the coordinates are distinct. The particles are listed in order of increasing of coordinates. All the coordinates are in meters, and all the velocities ΓÇö in meters per second. The negative velocity means that after the start of collider the particle will move to the left, and the positive ΓÇö that the particle will move to the right.

## Output

If there will be no big bang, output -1 . Otherwise output one number ΓÇö how much time in seconds elapses after the launch of the collider before the big bang happens. Your answer must have a relative or absolute error less than 10 ΓÇë-ΓÇë9 .

## Examples

Example 1:
```
3
-5 9
0 1
5 -1
```
```
1.00000000000000000000
```
