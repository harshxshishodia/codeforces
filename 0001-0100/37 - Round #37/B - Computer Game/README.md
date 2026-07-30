# B. Computer Game

**Submission:** https://codeforces.com/contest/37/problem/B

**Limits:** 1 second / 256 megabytes

## Problem Statement

VasyaΓÇÖs elder brother Petya loves playing computer games. In one of his favourite computer games Petya reached the final level where a fight with the boss take place.

While playing the game Petya found spell scrolls and now he is about to use them. LetΓÇÖs describe the way fighting goes on this level:

1) The boss has two parameters: max ΓÇö the initial amount of health and reg ΓÇö regeneration rate per second.

2) Every scroll also has two parameters: pow i ΓÇö spell power measured in percents ΓÇö the maximal amount of health counted off the initial one, which allows to use the scroll (i.e. if the boss has more than pow i percent of health the scroll cannot be used); and dmg i the damage per second inflicted upon the boss if the scroll is used. As soon as a scroll is used it disappears and another spell is cast upon the boss that inflicts dmg i of damage per second upon him until the end of the game.

During the battle the actions per second are performed in the following order: first the boss gets the damage from all the spells cast upon him, then he regenerates reg of health (at the same time he canΓÇÖt have more than max of health), then the player may use another scroll (no more than one per second).

The boss is considered to be defeated if at the end of a second he has nonpositive ( ΓÇëΓëñΓÇë0 ) amount of health.

Help Petya to determine whether he can win with the set of scrolls available to him and if he can, determine the minimal number of seconds he needs to do it.

## Input

The first line contains three integers N , max and reg ( 1ΓÇëΓëñΓÇë N ,ΓÇë max ,ΓÇë reg ΓÇëΓëñΓÇë1000 ) ΓÇôΓÇô the amount of scrolls and the parameters of the boss. The next N lines contain two integers pow i and dmg i each ΓÇö the parameters of the i -th scroll ( 0ΓÇëΓëñΓÇë pow i ΓÇëΓëñΓÇë100 , 1ΓÇëΓëñΓÇë dmg i ΓÇëΓëñΓÇë2000 ).

## Output

In case Petya canΓÇÖt complete this level, output in the single line NO .

Otherwise, output on the first line YES . On the second line output the minimal time after which the boss can be defeated and the number of used scrolls. In the next lines for each used scroll output space-separated number of seconds passed from the start of the battle to the moment the scroll was used and the number of the scroll. Scrolls are numbered starting from 1 in the input order. The first scroll is considered to be available to be used after 0 seconds.

Output scrolls in the order they were used. It is not allowed to use scrolls after the boss is defeated.

## Examples

Example 1:
```
2 10 3
100 3
99 1
```
```
NO
```
