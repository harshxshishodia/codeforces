# C. Page Numbers

**Submission:** https://codeforces.com/contest/34/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

┬½Bersoft┬╗ company is working on a new version of its most popular text editor ΓÇö Bord 2010. Bord, like many other text editors, should be able to print out multipage documents. A user keys a sequence of the document page numbers that he wants to print out (separates them with a comma, without spaces).

Your task is to write a part of the program, responsible for ┬½standardization┬╗ of this sequence. Your program gets the sequence, keyed by the user, as input. The program should output this sequence in format l 1 - r 1 , l 2 - r 2 ,..., l k - r k , where r i ΓÇë+ΓÇë1ΓÇë<ΓÇë l i ΓÇë+ΓÇë1 for all i from 1 to k ΓÇë-ΓÇë1 , and l i ΓÇëΓëñΓÇë r i . The new sequence should contain all the page numbers, keyed by the user, and nothing else. If some page number appears in the input sequence several times, its appearances, starting from the second one, should be ignored. If for some element i from the new sequence l i ΓÇë=ΓÇë r i , this element should be output as l i , and not as ┬½ l i ΓÇë-ΓÇë l i ┬╗.

For example, sequence 1,2,3,1,1,2,6,6,2 should be output as 1-3,6 .

## Input

The only line contains the sequence, keyed by the user. The sequence contains at least one and at most 100 positive integer numbers. It's guaranteed, that this sequence consists of positive integer numbers, not exceeding 1000, separated with a comma, doesn't contain any other characters, apart from digits and commas, can't end with a comma, and the numbers don't contain leading zeroes. Also it doesn't start with a comma or contain more than one comma in a row.

## Output

Output the sequence in the required format.

## Examples

Example 1:
```
1,2,3,1,1,2,6,6,2
```
```
1-3,6
```
