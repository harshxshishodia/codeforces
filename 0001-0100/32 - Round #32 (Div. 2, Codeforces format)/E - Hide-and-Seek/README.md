# E. Hide-and-Seek

**Submission:** https://codeforces.com/contest/32/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Victor and Peter are playing hide-and-seek. Peter has hidden, and Victor is to find him. In the room where they are playing, there is only one non-transparent wall and one double-sided mirror. Victor and Peter are points with coordinates ( x v ,ΓÇë y v ) and ( x p ,ΓÇë y p ) respectively. The wall is a segment joining points with coordinates ( x w ,ΓÇë1 ,ΓÇë y w ,ΓÇë1 ) and ( x w ,ΓÇë2 ,ΓÇë y w ,ΓÇë2 ) , the mirror ΓÇö a segment joining points ( x m ,ΓÇë1 ,ΓÇë y m ,ΓÇë1 ) and ( x m ,ΓÇë2 ,ΓÇë y m ,ΓÇë2 ) .

If an obstacle has a common point with a line of vision, it's considered, that the boys can't see each other with this line of vision. If the mirror has a common point with the line of vision, it's considered, that the boys can see each other in the mirror, i.e. reflection takes place. The reflection process is governed by laws of physics ΓÇö the angle of incidence is equal to the angle of reflection. The incident ray is in the same half-plane as the reflected ray, relative to the mirror. I.e. to see each other Victor and Peter should be to the same side of the line, containing the mirror (see example 1). If the line of vision is parallel to the mirror, reflection doesn't take place, and the mirror isn't regarded as an obstacle (see example 4).

Victor got interested if he can see Peter, while standing at the same spot. Help him solve this problem.

## Input

The first line contains two numbers x v and y v ΓÇö coordinates of Victor.

The second line contains two numbers x p and y p ΓÇö coordinates of Peter.

The third line contains 4 numbers x w ,ΓÇë1 , y w ,ΓÇë1 , x w ,ΓÇë2 , y w ,ΓÇë2 ΓÇö coordinates of the wall.

The forth line contains 4 numbers x m ,ΓÇë1 , y m ,ΓÇë1 , x m ,ΓÇë2 , y m ,ΓÇë2 ΓÇö coordinates of the mirror.

All the coordinates are integer numbers, and don't exceed 10 4 in absolute value. It's guaranteed, that the segments don't have common points, Victor and Peter are not on any of the segments, coordinates of Victor and Peter aren't the same, the segments don't degenerate into points.

## Output

Output YES , if Victor can see Peter without leaving the initial spot. Otherwise output NO .

## Examples

Example 1:
```
-1 3
1 3
0 2 0 4
0 0 0 1
```
```
NO
```
