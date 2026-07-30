# E. Beads

**Submission:** https://codeforces.com/contest/8/problem/E

**Limits:** 5 seconds / 64 megabytes

## Problem Statement

One Martian boy called Zorg wants to present a string of beads to his friend from the Earth ΓÇö Masha. He knows that Masha likes two colours: blue and red, ΓÇö and right in the shop where he has come, there is a variety of adornments with beads of these two colours. All the strings of beads have a small fastener, and if one unfastens it, one might notice that all the strings of beads in the shop are of the same length. Because of the peculiarities of the Martian eyesight, if Zorg sees one blue-and-red string of beads first, and then the other with red beads instead of blue ones, and blue ΓÇö instead of red, he regards these two strings of beads as identical. In other words, Zorg regards as identical not only those strings of beads that can be derived from each other by the string turnover, but as well those that can be derived from each other by a mutual replacement of colours and/or by the string turnover.

It is known that all Martians are very orderly, and if a Martian sees some amount of objects, he tries to put them in good order. Zorg thinks that a red bead is smaller than a blue one. Let's put 0 for a red bead, and 1 ΓÇö for a blue one. From two strings the Martian puts earlier the string with a red bead in the i -th position, providing that the second string has a blue bead in the i -th position, and the first two beads i ΓÇë-ΓÇë1 are identical.

At first Zorg unfastens all the strings of beads, and puts them into small heaps so, that in each heap strings are identical, in his opinion. Then he sorts out the heaps and chooses the minimum string in each heap, in his opinion. He gives the unnecassary strings back to the shop assistant and says he doesn't need them any more. Then Zorg sorts out the remaining strings of beads and buys the string with index k . 

All these manupulations will take Zorg a lot of time, that's why he asks you to help and find the string of beads for Masha.

## Input

The input file contains two integers n and k ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë50;1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë10 16 ) ΓÇöthe length of a string of beads, and the index of the string, chosen by Zorg.

## Output

Output the k -th string of beads, putting 0 for a red bead, and 1 ΓÇö for a blue one. If it s impossible to find the required string, output the only number -1 .

## Examples

Example 1:
```
4 4
```
```
0101
```

## Note

Let's consider the example of strings of length 4 ΓÇö 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110. Zorg will divide them into heaps: {0001, 0111, 1000, 1110}, {0010, 0100, 1011, 1101}, {0011, 1100}, {0101, 1010}, {0110, 1001}. Then he will choose the minimum strings of beads in each heap: 0001, 0010, 0011, 0101, 0110. The forth string ΓÇö 0101.
