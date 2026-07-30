# E. Contact

**Submission:** https://codeforces.com/contest/68/problem/E

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

Little Petya is preparing for the first contact with aliens. He knows that alien spaceships have shapes of non-degenerate triangles and there will be exactly 4 ships. Landing platform for a ship can be made of 3 special columns located at some points of a Cartesian plane such that these 3 points form a triangle equal to the ship with respect to rotations, translations (parallel shifts along some vector) and reflections (symmetries along the edges). The ships can overlap after the landing.

Each column can be used to land more than one ship, for example, if there are two equal ships, we don't need to build 6 columns to land both ships, 3 will be enough. Petya wants to know what minimum number of columns will be enough to land all ships.

## Input

Each of 4 lines will contain 6 integers x 1 y 1 x 2 y 2 x 3 y 3 ( 0ΓÇëΓëñΓÇë x 1 ,ΓÇë y 1 ,ΓÇë x 2 ,ΓÇë y 2 ,ΓÇë x 3 ,ΓÇë y 3 ΓÇëΓëñΓÇë20 ), representing 3 points that describe the shape of each of 4 ships. It is guaranteed that 3 points in each line will represent a non-degenerate triangle.

## Output

First line should contain minimum number of columns enough to land all spaceships.

## Examples

Example 1:
```
0 0 1 0 1 2
0 0 0 2 2 2
0 0 3 0 1 2
0 0 3 0 2 2
```
```
4
```

## Note

In the first test case columns can be put in these points: (0,ΓÇë0),ΓÇë(1,ΓÇë0),ΓÇë(3,ΓÇë0),ΓÇë(1,ΓÇë2) . Note that the second ship can land using last 3 columns.

In the second test case following points can be chosen: (0,ΓÇë0),ΓÇë(0,ΓÇë1),ΓÇë(1,ΓÇë0),ΓÇë(0,ΓÇë2),ΓÇë(2,ΓÇë0),ΓÇë(0,ΓÇë5),ΓÇë(5,ΓÇë0),ΓÇë(0,ΓÇë17),ΓÇë(17,ΓÇë0) . It is impossible to use less than 9 columns.
