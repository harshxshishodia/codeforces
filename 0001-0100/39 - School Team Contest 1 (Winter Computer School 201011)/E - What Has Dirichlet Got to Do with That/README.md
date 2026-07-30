# E. What Has Dirichlet Got to Do with That?

**Submission:** https://codeforces.com/contest/39/problem/E

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

You all know the Dirichlet principle, the point of which is that if n boxes have no less than n ΓÇë+ΓÇë1 items, that leads to the existence of a box in which there are at least two items.

Having heard of that principle, but having not mastered the technique of logical thinking, 8 year olds Stas and Masha invented a game. There are a different boxes and b different items, and each turn a player can either add a new box or a new item. The player, after whose turn the number of ways of putting b items into a boxes becomes no less then a certain given number n , loses. All the boxes and items are considered to be different. Boxes may remain empty.

Who loses if both players play optimally and Stas's turn is first?

## Input

The only input line has three integers a ,ΓÇë b ,ΓÇë n ( 1ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë10000 , 1ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë30 , 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 9 ) ΓÇö the initial number of the boxes, the number of the items and the number which constrains the number of ways, respectively. Guaranteed that the initial number of ways is strictly less than n .

## Output

Output "Stas" if Masha wins. Output "Masha" if Stas wins. In case of a draw, output "Missing".

## Examples

Example 1:
```
2 2 10
```
```
Masha
```

## Note

In the second example the initial number of ways is equal to 3125 . 

 
- If Stas increases the number of boxes, he will lose, as Masha may increase the number of boxes once more during her turn. After that any Stas's move will lead to defeat. 
- But if Stas increases the number of items, then any Masha's move will be losing.
