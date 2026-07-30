# B. Mice

**Submission:** https://codeforces.com/contest/76/problem/B

**Limits:** 0.5 second / 256 megabytes

## Problem Statement

Modern researches has shown that a flock of hungry mice searching for a piece of cheese acts as follows: if there are several pieces of cheese then each mouse chooses the closest one. After that all mice start moving towards the chosen piece of cheese. When a mouse or several mice achieve the destination point and there is still a piece of cheese in it, they eat it and become well-fed. Each mice that reaches this point after that remains hungry. Moving speeds of all mice are equal.

If there are several ways to choose closest pieces then mice will choose it in a way that would minimize the number of hungry mice. To check this theory scientists decided to conduct an experiment. They located N mice and M pieces of cheese on a cartesian plane where all mice are located on the line y ΓÇë=ΓÇë Y 0 and all pieces of cheese ΓÇö on another line y ΓÇë=ΓÇë Y 1 . To check the results of the experiment the scientists need a program which simulates the behavior of a flock of hungry mice.

Write a program that computes the minimal number of mice which will remain hungry, i.e. without cheese.

## Input

The first line of the input contains four integer numbers N ( 1ΓÇëΓëñΓÇë N ΓÇëΓëñΓÇë10 5 ), M ( 0ΓÇëΓëñΓÇë M ΓÇëΓëñΓÇë10 5 ), Y 0 ( 0ΓÇëΓëñΓÇë Y 0 ΓÇëΓëñΓÇë10 7 ), Y 1 ( 0ΓÇëΓëñΓÇë Y 1 ΓÇëΓëñΓÇë10 7 , Y 0 ΓÇëΓëáΓÇë Y 1 ). The second line contains a strictly increasing sequence of N numbers ΓÇö x coordinates of mice. Third line contains a strictly increasing sequence of M numbers ΓÇö x coordinates of cheese. All coordinates are integers and do not exceed 10 7 by absolute value.

## Output

The only line of output should contain one number ΓÇö the minimal number of mice which will remain without cheese.

## Examples

Example 1:
```
3 2 0 2
0 1 3
2 5
```
```
1
```

## Note

All the three mice will choose the first piece of cheese. Second and third mice will eat this piece. The first one will remain hungry, because it was running towards the same piece, but it was late. The second piece of cheese will remain uneaten.
