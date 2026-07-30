# K. Testing

**Submission:** https://codeforces.com/contest/39/problem/K

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

You take part in the testing of new weapon. For the testing a polygon was created. The polygon is a rectangular field n ΓÇë├ùΓÇë m in size, divided into unit squares 1ΓÇë├ùΓÇë1 in size. The polygon contains k objects, each of which is a rectangle with sides, parallel to the polygon sides and entirely occupying several unit squares. The objects don't intersect and don't touch each other.

The principle according to which the weapon works is highly secret. You only know that one can use it to strike any rectangular area whose area is not equal to zero with sides, parallel to the sides of the polygon. The area must completely cover some of the unit squares into which the polygon is divided and it must not touch the other squares. Of course the area mustn't cross the polygon border. Your task is as follows: you should hit no less than one and no more than three rectangular objects. Each object must either lay completely inside the area (in that case it is considered to be hit), or lay completely outside the area.

Find the number of ways of hitting.

## Input

The first line has three integers n , m ╨╕ k ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë1000 , 1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë90 ) ΓÇö the sizes of the polygon and the number of objects on it respectively. Next n lines contain m symbols each and describe the polygon. The symbol " * " stands for a square occupied an object, whereas the symbol " . " stands for an empty space. The symbols " * " form exactly k rectangular connected areas that meet the requirements of the task.

## Output

Output a single number ΓÇö the number of different ways to hit a target.

## Examples

Example 1:
```
3 3 3
*.*
...
*..
```
```
21
```
