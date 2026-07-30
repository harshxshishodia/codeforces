# C. LionAge II

**Submission:** https://codeforces.com/contest/73/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya plays the LionAge II. He was bored of playing with a stupid computer, so he installed this popular MMORPG, to fight with his friends. Vasya came up with the name of his character ΓÇö non-empty string s , consisting of a lowercase Latin letters. However, in order not to put up a front of friends, Vasya has decided to change no more than k letters of the character name so that the new name sounded as good as possible. Euphony of the line is defined as follows: for each pair of adjacent letters x and y ( x immediately precedes y ) the bonus c ( x ,ΓÇë y ) is added to the result. Your task is to determine what the greatest Euphony can be obtained by changing at most k letters in the name of the Vasya's character.

## Input

The first line contains character's name s and an integer number k ( 0ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë100 ). The length of the nonempty string s does not exceed 100 . The second line contains an integer number n ( 0ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë676 ) ΓÇö amount of pairs of letters, giving bonus to the euphony. The next n lines contain description of these pairs ┬½ x y c ┬╗, which means that sequence xy gives bonus c ( x ,ΓÇë y ΓÇö lowercase Latin letters, ΓÇë-ΓÇë1000ΓÇëΓëñΓÇë c ΓÇëΓëñΓÇë1000) . It is guaranteed that no pair x y mentioned twice in the input data.

## Output

Output the only number ΓÇö maximum possible euphony ╨╛f the new character's name.

## Examples

Example 1:
```
winner 4
4
s e 7
o s 8
l o 13
o o 8
```
```
36
```

## Note

In the first example the most euphony name will be looser . It is easy to calculate that its euphony is 36.
