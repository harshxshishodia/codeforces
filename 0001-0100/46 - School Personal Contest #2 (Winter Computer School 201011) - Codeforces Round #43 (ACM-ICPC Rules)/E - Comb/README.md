# E. Comb

**Submission:** https://codeforces.com/contest/46/problem/E

**Limits:** 1 second / 256 megabytes

## Problem Statement

Having endured all the hardships, Lara Croft finally found herself in a room with treasures. To her surprise she didn't find golden mountains there. Lara looked around and noticed on the floor a painted table n ΓÇë├ùΓÇë m panels in size with integers written on the panels. There also was a huge number of stones lying by the wall. On the pillar near the table Lara found a guidance note which said that to get hold of the treasures one has to choose some non-zero number of the first panels in each row of the table and put stones on all those panels to push them down. After that she will receive a number of golden coins equal to the sum of numbers written on the chosen panels. Lara quickly made up her mind on how to arrange the stones and was about to start when she noticed an addition to the note in small font below. According to the addition, for the room ceiling not to crush and smash the adventurer, the chosen panels should form a comb. It was explained that the chosen panels form a comb when the sequence c 1 ,ΓÇë c 2 ,ΓÇë...,ΓÇë c n made from the quantities of panels chosen in each table line satisfies the following property: c 1 ΓÇë>ΓÇë c 2 ΓÇë<ΓÇë c 3 ΓÇë>ΓÇë c 4 ΓÇë<ΓÇë... , i.e. the inequation mark interchanges between the neighboring elements. Now Lara is bewildered and doesn't know what to do. Help her to determine the largest number of coins she can get and survive at the same time.

## Input

The first line contains a pair of integers n ,ΓÇë m ( 2ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë1500 ). Next n lines contain m integers each ΓÇö that is the table itself. The absolute value of the numbers in the table does not exceed 10000 .

## Output

Print the single number ΓÇö the maximum number of coins Lara can get.

## Examples

Example 1:
```
2 2
-1 2
1 3
```
```
2
```
