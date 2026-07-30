# A. Hockey

**Submission:** https://codeforces.com/contest/95/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Petya loves hockey very much. One day, as he was watching a hockey match, he fell asleep. Petya dreamt of being appointed to change a hockey team's name. Thus, Petya was given the original team name w and the collection of forbidden substrings s 1 ,ΓÇë s 2 ,ΓÇë...,ΓÇë s n . All those strings consist of uppercase and lowercase Latin letters. String w has the length of | w | , its characters are numbered from 1 to | w | .

First Petya should find all the occurrences of forbidden substrings in the w string. During the search of substrings the case of letter shouldn't be taken into consideration. That is, strings " aBC " and " ABc " are considered equal.

After that Petya should perform the replacement of all letters covered by the occurrences. More formally: a letter in the position i should be replaced by any other one if for position i in string w there exist pair of indices l ,ΓÇë r ( 1ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë r ΓÇëΓëñΓÇë| w | ) such that substring w [ l ┬á...┬á r ] is contained in the collection s 1 ,ΓÇë s 2 ,ΓÇë...,ΓÇë s n , when using case insensitive comparison. During the replacement the letter's case should remain the same. Petya is not allowed to replace the letters that aren't covered by any forbidden substring.

Letter letter (uppercase or lowercase) is considered lucky for the hockey players. That's why Petya should perform the changes so that the letter occurred in the resulting string as many times as possible. Help Petya to find such resulting string. If there are several such strings, find the one that comes first lexicographically.

Note that the process of replacements is not repeated, it occurs only once. That is, if after Petya's replacements the string started to contain new occurrences of bad substrings, Petya pays no attention to them.

## Input

The first line contains the only integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the number of forbidden substrings in the collection. Next n lines contain these substrings. The next line contains string w . All those n ΓÇë+ΓÇë1 lines are non-empty strings consisting of uppercase and lowercase Latin letters whose length does not exceed 100 . The last line contains a lowercase letter letter .

## Output

Output the only line ΓÇö Petya's resulting string with the maximum number of letters letter . If there are several answers then output the one that comes first lexicographically.

The lexicographical comparison is performed by the standard < operator in modern programming languages. The line a is lexicographically smaller than the line b , if a is a prefix of b , or there exists such an i ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë| a | ), that a i ΓÇë<ΓÇë b i , and for any j ( 1ΓÇëΓëñΓÇë j ΓÇë<ΓÇë i ) a j ΓÇë=ΓÇë b j . | a | stands for the length of string a .

## Examples

Example 1:
```
3
bers
ucky
elu
PetrLoveLuckyNumbers
t
```
```
PetrLovtTttttNumtttt
```
