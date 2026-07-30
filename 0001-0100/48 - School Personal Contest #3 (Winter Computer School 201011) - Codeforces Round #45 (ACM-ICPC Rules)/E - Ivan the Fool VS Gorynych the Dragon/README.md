# E. Ivan the Fool VS Gorynych the Dragon

**Submission:** https://codeforces.com/contest/48/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Once upon a time in a kingdom far, far awayΓÇª Okay, letΓÇÖs start at the point where Ivan the Fool met Gorynych the Dragon. Ivan took out his magic sword and the battle began. First Gorynych had h heads and t tails. With each strike of the sword Ivan can either cut off several heads (from 1 to n , but not more than Gorynych has at the moment), or several tails (from 1 to m , but not more than Gorynych has at the moment). At the same time, horrible though it seems, Gorynych the Dragon can also grow new heads and tails. And the number of growing heads and tails is determined uniquely by the number of heads or tails cut by the current strike. When the total number of heads and tails exceeds R , Gorynych the Dragon strikes its final blow and destroys Ivan the Fool. ThatΓÇÖs why Ivan aims to cut off all the dragonΓÇÖs heads and tails as quickly as possible and win. The events can also develop in a third way: neither of the opponents can win over the other one and they will continue fighting forever.

The tale goes like this; easy to say, hard to do. Your task is to write a program that will determine the battleΓÇÖs outcome. Consider that Ivan strikes consecutively. After each blow Gorynych grows a number of new heads and tails depending on the number of cut ones. Gorynych the Dragon is defeated if after the blow he loses all his heads and tails and canΓÇÖt grow new ones. Ivan fights in the optimal way (fools are lucky), i.e. 

 
- if Ivan can win, he wins having struck the least number of blows; 
- if it is impossible to defeat Gorynych, but is possible to resist him for an infinitely long period of time, then thatΓÇÖs the strategy Ivan chooses; 
- if Gorynych wins in any case, Ivan aims to resist him for as long as possible.

## Input

The first line contains three integers h , t and R ( 0ΓÇëΓëñΓÇë h ,ΓÇë t ,ΓÇë R ΓÇëΓëñΓÇë200 , 0ΓÇë<ΓÇë h ΓÇë+ΓÇë t ΓÇëΓëñΓÇë R ) which represent the initial numbers of GorynychΓÇÖs heads and tails and the largest total number of heads and tails with which Gorynych the Dragon does not yet attack. The next line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë200 ). The next n contain pairs of non-negative numbers " h i t i " which represent the number of heads and the number of tails correspondingly, that will grow if Gorynych has i heads ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ) cut. The next line contains an integer m ( 1ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë200 ) and then ΓÇö the description of GorynychΓÇÖs behavior when his tails are cut off in the format identical to the one described above. All the numbers in the input file do not exceed 200 .

## Output

Print "Ivan" (without quotes) in the first line if Ivan wins, or "Zmey" (that means a dragon in Russian) if Gorynych the Dragon wins. In the second line print a single integer which represents the number of blows Ivan makes. If the battle will continue forever, print in the first line "Draw".

## Examples

Example 1:
```
2 2 4
2
1 0
0 1
3
0 1
0 1
0 0
```
```
Ivan
2
```
