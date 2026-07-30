# B. Laser

**Submission:** https://codeforces.com/contest/15/problem/B

**Limits:** 1 second / 64 megabytes

## Problem Statement

Petya is the most responsible worker in the Research Institute. So he was asked to make a very important experiment: to melt the chocolate bar with a new laser device. The device consists of a rectangular field of n ΓÇë├ùΓÇë m cells and a robotic arm. Each cell of the field is a 1ΓÇë├ùΓÇë1 square. The robotic arm has two lasers pointed at the field perpendicularly to its surface. At any one time lasers are pointed at the centres of some two cells. Since the lasers are on the robotic hand, their movements are synchronized ΓÇö if you move one of the lasers by a vector, another one moves by the same vector.

The following facts about the experiment are known: 

 
- initially the whole field is covered with a chocolate bar of the size n ΓÇë├ùΓÇë m , both lasers are located above the field and are active; 
- the chocolate melts within one cell of the field at which the laser is pointed; 
- all moves of the robotic arm should be parallel to the sides of the field, after each move the lasers should be pointed at the centres of some two cells; 
- at any one time both lasers should be pointed at the field. Petya doesn't want to become a second Gordon Freeman. 

You are given n , m and the cells ( x 1 ,ΓÇë y 1 ) and ( x 2 ,ΓÇë y 2 ) , where the lasers are initially pointed at ( x i is a column number, y i is a row number). Rows are numbered from 1 to m from top to bottom and columns are numbered from 1 to n from left to right. You are to find the amount of cells of the field on which the chocolate can't be melted in the given conditions.

## Input

The first line contains one integer number t (1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë10000) ΓÇö the number of test sets. Each of the following t lines describes one test set. Each line contains integer numbers n , m , x 1 , y 1 , x 2 , y 2 , separated by a space ( 2ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë10 9 , 1ΓÇëΓëñΓÇë x 1 ,ΓÇë x 2 ΓÇëΓëñΓÇë n , 1ΓÇëΓëñΓÇë y 1 ,ΓÇë y 2 ΓÇëΓëñΓÇë m ). Cells ( x 1 ,ΓÇë y 1 ) and ( x 2 ,ΓÇë y 2 ) are distinct.

## Output

Each of the t lines of the output should contain the answer to the corresponding input test set.

## Examples

Example 1:
```
2
4 4 1 1 3 3
4 3 1 1 2 2
```
```
8
2
```
