# C. Genetic engineering

**Submission:** https://codeforces.com/contest/86/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

"Multidimensional spaces are completely out of style these days, unlike genetics problems" ΓÇö thought physicist Woll and changed his subject of study to bioinformatics. Analysing results of sequencing he faced the following problem concerning DNA sequences. We will further think of a DNA sequence as an arbitrary string of uppercase letters " A ", " C ", " G " and " T " (of course, this is a simplified interpretation).

Let w be a long DNA sequence and s 1 ,ΓÇë s 2 ,ΓÇë...,ΓÇë s m ΓÇö collection of short DNA sequences. Let us say that the collection filters w iff w can be covered with the sequences from the collection. Certainly, substrings corresponding to the different positions of the string may intersect or even cover each other. More formally: denote by | w | the length of w , let symbols of w be numbered from 1 to | w | . Then for each position i in w there exist pair of indices l ,ΓÇë r ( 1ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë r ΓÇëΓëñΓÇë| w | ) such that the substring w [ l ┬á...┬á r ] equals one of the elements s 1 ,ΓÇë s 2 ,ΓÇë...,ΓÇë s m of the collection.

Woll wants to calculate the number of DNA sequences of a given length filtered by a given collection, but he doesn't know how to deal with it. Help him! Your task is to find the number of different DNA sequences of length n filtered by the collection { s i } .

Answer may appear very large, so output it modulo 1000000009 .

## Input

First line contains two integer numbers n and m ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000,ΓÇë1ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10 ) ΓÇö the length of the string and the number of sequences in the collection correspondently. 

Next m lines contain the collection sequences s i , one per line. Each s i is a nonempty string of length not greater than 10 . All the strings consist of uppercase letters " A ", " C ", " G ", " T ". The collection may contain identical strings.

## Output

Output should contain a single integer ΓÇö the number of strings filtered by the collection modulo 1000000009 ( 10 9 ΓÇë+ΓÇë9 ).

## Examples

Example 1:
```
2 1
A
```
```
1
```

## Note

In the first sample, a string has to be filtered by " A ". Clearly, there is only one such string: " AA ".

In the second sample, there exist exactly two different strings satisfying the condition (see the pictures below).
