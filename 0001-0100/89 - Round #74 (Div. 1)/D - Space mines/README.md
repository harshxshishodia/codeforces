# D. Space mines

**Submission:** https://codeforces.com/contest/89/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Once upon a time in the galaxy of far, far away...

Darth Wader found out the location of a rebels' base. Now he is going to destroy the base (and the whole planet that the base is located at), using the Death Star.

When the rebels learnt that the Death Star was coming, they decided to use their new secret weapon ΓÇö space mines. Let's describe a space mine's build.

Each space mine is shaped like a ball (we'll call it the mine body) of a certain radius r with the center in the point O . Several spikes protrude from the center. Each spike can be represented as a segment, connecting the center of the mine with some point P , such that (transporting long-spiked mines is problematic), where | OP | is the length of the segment connecting O and P . It is convenient to describe the point P by a vector p such that P ΓÇë=ΓÇë O ΓÇë+ΓÇë p .

The Death Star is shaped like a ball with the radius of R ( R exceeds any mine's radius). It moves at a constant speed along the v vector at the speed equal to | v | . At the moment the rebels noticed the Star of Death, it was located in the point A .

The rebels located n space mines along the Death Star's way. You may regard the mines as being idle. The Death Star does not know about the mines' existence and cannot notice them, which is why it doesn't change the direction of its movement. As soon as the Star of Death touched the mine (its body or one of the spikes), the mine bursts and destroys the Star of Death. A touching is the situation when there is a point in space which belongs both to the mine and to the Death Star. It is considered that Death Star will not be destroyed if it can move infinitely long time without touching the mines.

Help the rebels determine whether they will succeed in destroying the Death Star using space mines or not. If they will succeed, determine the moment of time when it will happen (starting from the moment the Death Star was noticed).

## Input

The first input data line contains 7 integers A x ,ΓÇë A y ,ΓÇë A z ,ΓÇë v x ,ΓÇë v y ,ΓÇë v z ,ΓÇë R . They are the Death Star's initial position, the direction of its movement, and its radius ( ΓÇë-ΓÇë10ΓÇëΓëñΓÇë v x ,ΓÇë v y ,ΓÇë v z ΓÇëΓëñΓÇë10 , | v |ΓÇë>ΓÇë0 , 0ΓÇë<ΓÇë R ΓÇëΓëñΓÇë100 ).

The second line contains an integer n , which is the number of mines ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ). Then follow n data blocks, the i -th of them describes the i -th mine.

The first line of each block contains 5 integers O ix ,ΓÇë O iy ,ΓÇë O iz ,ΓÇë r i ,ΓÇë m i , which are the coordinates of the mine centre, the radius of its body and the number of spikes ( 0ΓÇë<ΓÇë r i ΓÇë<ΓÇë100,ΓÇë0ΓÇëΓëñΓÇë m i ΓÇëΓëñΓÇë10 ). Then follow m i lines, describing the spikes of the i -th mine, where the j -th of them describes the i -th spike and contains 3 integers p ijx ,ΓÇë p ijy ,ΓÇë p ijz ΓÇö the coordinates of the vector where the given spike is directed ( ).

The coordinates of the mines' centers and the center of the Death Star are integers, their absolute value does not exceed 10000 . It is guaranteed that R ΓÇë>ΓÇë r i for any 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n . For any mines i ΓÇëΓëáΓÇë j the following inequality if fulfilled: . Initially the Death Star and the mines do not have common points.

## Output

If the rebels will succeed in stopping the Death Star using space mines, print the time from the moment the Death Star was noticed to the blast.

If the Death Star will not touch a mine, print "-1" (without quotes).

For the answer the absolute or relative error of 10 ΓÇë-ΓÇë6 is acceptable.

## Examples

Example 1:
```
0 0 0 1 0 0 5
2
10 8 0 2 2
0 -3 0
2 2 0
20 0 0 4 3
2 4 0
-4 3 0
1 -5 0
```
```
10.0000000000
```
