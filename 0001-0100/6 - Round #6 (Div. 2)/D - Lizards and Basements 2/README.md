# D. Lizards and Basements 2

**Submission:** https://codeforces.com/contest/6/problem/D

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

This is simplified version of the problem used on the original contest. The original problem seems to have too difiicult solution. The constraints for input data have been reduced. 

Polycarp likes to play computer role-playing game ┬½Lizards and Basements┬╗. At the moment he is playing it as a magician. At one of the last levels he has to fight the line of archers. The only spell with which he can damage them is a fire ball. If Polycarp hits the i -th archer with his fire ball (they are numbered from left to right), the archer loses a health points. At the same time the spell damages the archers adjacent to the i -th (if any) ΓÇö they lose b ( 1ΓÇëΓëñΓÇë b ΓÇë<ΓÇë a ΓÇëΓëñΓÇë10 ) health points each.

As the extreme archers (i.e. archers numbered 1 and n ) are very far, the fire ball cannot reach them. Polycarp can hit any other archer with his fire ball.

The amount of health points for each archer is known. An archer will be killed when this amount is less than 0. What is the minimum amount of spells Polycarp can use to kill all the enemies?

Polycarp can throw his fire ball into an archer if the latter is already killed.

## Input

The first line of the input contains three integers n ,ΓÇë a ,ΓÇë b ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 ; 1ΓÇëΓëñΓÇë b ΓÇë<ΓÇë a ΓÇëΓëñΓÇë10 ). The second line contains a sequence of n integers ΓÇö h 1 ,ΓÇë h 2 ,ΓÇë...,ΓÇë h n ( 1ΓÇëΓëñΓÇë h i ΓÇëΓëñΓÇë15 ), where h i is the amount of health points the i -th archer has.

## Output

In the first line print t ΓÇö the required minimum amount of fire balls.

In the second line print t numbers ΓÇö indexes of the archers that Polycarp should hit to kill all the archers in t shots. All these numbers should be between 2 and n ΓÇë-ΓÇë1 . Separate numbers with spaces. If there are several solutions, output any of them. Print numbers in any order.

## Examples

Example 1:
```
3 2 1
2 2 2
```
```
3
2 2 2
```
