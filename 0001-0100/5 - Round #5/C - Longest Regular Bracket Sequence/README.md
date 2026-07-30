# C. Longest Regular Bracket Sequence

**Submission:** https://codeforces.com/contest/5/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

This is yet another problem dealing with regular bracket sequences.

We should remind you that a bracket sequence is called regular, if by inserting ┬½ + ┬╗ and ┬½ 1 ┬╗ into it we can get a correct mathematical expression. For example, sequences ┬½ (())() ┬╗, ┬½ () ┬╗ and ┬½ (()(())) ┬╗ are regular, while ┬½ )( ┬╗, ┬½ (() ┬╗ and ┬½ (()))( ┬╗ are not. 

You are given a string of ┬½ ( ┬╗ and ┬½ ) ┬╗ characters. You are to find its longest substring that is a regular bracket sequence. You are to find the number of such substrings as well.

## Input

The first line of the input file contains a non-empty string, consisting of ┬½ ( ┬╗ and ┬½ ) ┬╗ characters. Its length does not exceed 10 6 .

## Output

Print the length of the longest substring that is a regular bracket sequence, and the number of such substrings. If there are no such substrings, write the only line containing " 0 1 ".

## Examples

Example 1:
```
)((())))(()())
```
```
6 2
```
