# C. Old Berland Language

**Submission:** https://codeforces.com/contest/37/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Berland scientists know that the Old Berland language had exactly n words. Those words had lengths of l 1 ,ΓÇë l 2 ,ΓÇë...,ΓÇë l n letters. Every word consisted of two letters, 0 and 1 . Ancient Berland people spoke quickly and didnΓÇÖt make pauses between the words, but at the same time they could always understand each other perfectly. It was possible because no word was a prefix of another one. The prefix of a string is considered to be one of its substrings that starts from the initial symbol.

Help the scientists determine whether all the words of the Old Berland language can be reconstructed and if they can, output the words themselves.

## Input

The first line contains one integer N ( 1ΓÇëΓëñΓÇë N ΓÇëΓëñΓÇë1000 ) ΓÇö the number of words in Old Berland language. The second line contains N space-separated integers ΓÇö the lengths of these words. All the lengths are natural numbers not exceeding 1000 .

## Output

If thereΓÇÖs no such set of words, in the single line output NO . Otherwise, in the first line output YES , and in the next N lines output the words themselves in the order their lengths were given in the input file. If the answer is not unique, output any.

## Examples

Example 1:
```
3
1 2 3
```
```
YES
0
10
110
```
