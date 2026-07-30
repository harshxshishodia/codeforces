# B. Young Photographer

**Submission:** https://codeforces.com/contest/14/problem/B

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

Among other things, Bob is keen on photography. Especially he likes to take pictures of sportsmen. That was the reason why he placed himself in position x 0 of a long straight racetrack and got ready to take pictures. But the problem was that not all the runners passed him. The total amount of sportsmen, training at that racetrack, equals n . And each of them regularly runs distances within a particular segment of the racetrack, which is the same for each sportsman. For example, the first sportsman runs from position a 1 to position b 1 , the second ΓÇö from a 2 to b 2 

What is the minimum distance that Bob should move to have a chance to take pictures of each sportsman? Bob can take a picture of a sportsman, if he stands within the segment that this sportsman covers on the racetrack.

## Input

The first line of the input file contains integers n and x 0 ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ; 0ΓÇëΓëñΓÇë x 0 ΓÇëΓëñΓÇë1000 ). The following n lines contain pairs of integers a i ,ΓÇë b i ( 0ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë1000 ; a i ΓÇëΓëáΓÇë b i ).

## Output

Output the required minimum distance in the same units as the positions on the racetrack. If there is no such a position, output -1.

## Examples

Example 1:
```
3 3
0 7
14 2
4 6
```
```
1
```
