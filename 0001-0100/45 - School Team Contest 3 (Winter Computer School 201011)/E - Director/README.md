# E. Director

**Submission:** https://codeforces.com/contest/45/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya is a born Berland film director, he is currently working on a new blockbuster, "The Unexpected". Vasya knows from his own experience how important it is to choose the main characters' names and surnames wisely. He made up a list of n names and n surnames that he wants to use. Vasya haven't decided yet how to call characters, so he is free to match any name to any surname. Now he has to make the list of all the main characters in the following format: " Name 1 Surname 1 , Name 2 Surname 2 , ... , Name n Surname n ", i.e. all the name-surname pairs should be separated by exactly one comma and exactly one space, and the name should be separated from the surname by exactly one space. First of all Vasya wants to maximize the number of the pairs, in which the name and the surname start from one letter. If there are several such variants, Vasya wants to get the lexicographically minimal one. Help him.

An answer will be verified a line in the format as is shown above, including the needed commas and spaces. It's the lexicographical minimality of such a line that needs to be ensured. The output line shouldn't end with a space or with a comma .

## Input

The first input line contains number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ) ΓÇö the number of names and surnames. Then follow n lines ΓÇö the list of names. Then follow n lines ΓÇö the list of surnames. No two from those 2 n strings match. Every name and surname is a non-empty string consisting of no more than 10 Latin letters. It is guaranteed that the first letter is uppercase and the rest are lowercase.

## Output

The output data consist of a single line ΓÇö the needed list. Note that one should follow closely the output data format!

## Examples

Example 1:
```
4
Ann
Anna
Sabrina
John
Petrov
Ivanova
Stoltz
Abacaba
```
```
Ann Abacaba, Anna Ivanova, John Petrov, Sabrina Stoltz
```
