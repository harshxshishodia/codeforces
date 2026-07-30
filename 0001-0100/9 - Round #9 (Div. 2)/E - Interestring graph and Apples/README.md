# E. Interesting Graph and Apples

**Submission:** https://codeforces.com/contest/9/problem/E

**Limits:** 1 second / 64 megabytes

## Problem Statement

Hexadecimal likes drawing. She has drawn many graphs already, both directed and not. Recently she has started to work on a still-life ┬½interesting graph and apples┬╗. An undirected graph is called interesting, if each of its vertices belongs to one cycle only ΓÇö a funny ring ΓÇö and does not belong to any other cycles. A funny ring is a cycle that goes through all the vertices just once. Moreover, loops are funny rings too.

She has already drawn the apples and some of the graph edges. But now it is not clear, how to connect the rest of the vertices to get an interesting graph as a result. The answer should contain the minimal amount of added edges. And furthermore, the answer should be the lexicographically smallest one. The set of edges ( x 1 ,ΓÇë y 1 ),ΓÇë( x 2 ,ΓÇë y 2 ),ΓÇë...,ΓÇë( x n ,ΓÇë y n ) , where x i ΓÇëΓëñΓÇë y i , is lexicographically smaller than the set ( u 1 ,ΓÇë v 1 ),ΓÇë( u 2 ,ΓÇë v 2 ),ΓÇë...,ΓÇë( u n ,ΓÇë v n ) , where u i ΓÇëΓëñΓÇë v i , provided that the sequence of integers x 1 ,ΓÇë y 1 ,ΓÇë x 2 ,ΓÇë y 2 ,ΓÇë...,ΓÇë x n ,ΓÇë y n is lexicographically smaller than the sequence u 1 ,ΓÇë v 1 ,ΓÇë u 2 ,ΓÇë v 2 ,ΓÇë...,ΓÇë u n ,ΓÇë v n . If you do not cope, Hexadecimal will eat you. ...eat you alive.

## Input

The first line of the input data contains a pair of integers n and m ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë50 , 0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë2500 ) ΓÇö the amount of vertices and edges respectively. The following lines contain pairs of numbers x i and y i ( 1ΓÇëΓëñΓÇë x i , y i ΓÇëΓëñΓÇë n ) ΓÇö the vertices that are already connected by edges. The initial graph may contain multiple edges and loops.

## Output

In the first line output ┬½ YES ┬╗ or ┬½ NO ┬╗: if it is possible or not to construct an interesting graph. If the answer is ┬½ YES ┬╗, in the second line output k ΓÇö the amount of edges that should be added to the initial graph. Finally, output k lines: pairs of vertices x j and y j , between which edges should be drawn. The result may contain multiple edges and loops. k can be equal to zero.

## Examples

Example 1:
```
3 2
1 2
2 3
```
```
YES
1
1 3
```
