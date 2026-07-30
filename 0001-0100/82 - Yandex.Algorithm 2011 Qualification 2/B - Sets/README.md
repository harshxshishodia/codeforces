# B. Sets

**Submission:** https://codeforces.com/contest/82/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Little Vasya likes very much to play with sets consisting of positive integers. To make the game more interesting, Vasya chose n non-empty sets in such a way, that no two of them have common elements.

One day he wanted to show his friends just how interesting playing with numbers is. For that he wrote out all possible unions of two different sets on n ┬╖( n ΓÇë-ΓÇë1)ΓÇë/ΓÇë2 pieces of paper. Then he shuffled the pieces of paper. He had written out the numbers in the unions in an arbitrary order.

For example, if n ΓÇë=ΓÇë4 , and the actual sets have the following form {1,ΓÇë3} , {5} , {2,ΓÇë4} , {7} , then the number of set pairs equals to six. The six pieces of paper can contain the following numbers: 

 
- 2,ΓÇë7,ΓÇë4 . 
- 1,ΓÇë7,ΓÇë3 ; 
- 5,ΓÇë4,ΓÇë2 ; 
- 1,ΓÇë3,ΓÇë5 ; 
- 3,ΓÇë1,ΓÇë2,ΓÇë4 ; 
- 5,ΓÇë7 . 

Then Vasya showed the pieces of paper to his friends, but kept the n sets secret from them. His friends managed to calculate which sets Vasya had thought of in the first place. And how about you, can you restore the sets by the given pieces of paper?

## Input

The first input file line contains a number n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë200 ), n is the number of sets at Vasya's disposal. Then follow sets of numbers from the pieces of paper written on n ┬╖( n ΓÇë-ΓÇë1)ΓÇë/ΓÇë2 lines. Each set starts with the number k i ( 2ΓÇëΓëñΓÇë k i ΓÇëΓëñΓÇë200 ), which is the number of numbers written of the i -th piece of paper, and then follow k i numbers a ij ( 1ΓÇëΓëñΓÇë a ij ΓÇëΓëñΓÇë200 ). All the numbers on the lines are separated by exactly one space. It is guaranteed that the input data is constructed according to the above given rules from n non-intersecting sets.

## Output

Print on n lines Vasya's sets' description. The first number on the line shows how many numbers the current set has. Then the set should be recorded by listing its elements. Separate the numbers by spaces. Each number and each set should be printed exactly once. Print the sets and the numbers in the sets in any order. If there are several answers to that problem, print any of them.

It is guaranteed that there is a solution.

## Examples

Example 1:
```
4
3 2 7 4
3 1 7 3
3 5 4 2
3 1 3 5
4 3 1 2 4
2 5 7
```
```
1 7 
2 2 4 
2 1 3 
1 5
```
