# B. Martian Architecture

**Submission:** https://codeforces.com/contest/57/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Chris the Rabbit found the traces of an ancient Martian civilization. The brave astronomer managed to see through a small telescope an architecture masterpiece ΓÇö "A Road to the Sun". The building stands on cubical stones of the same size. The foundation divides the entire "road" into cells, into which the cubical stones are fit tightly. Thus, to any cell of the foundation a coordinate can be assigned. To become the leader of the tribe, a Martian should build a Road to the Sun, that is to build from those cubical stones on a given foundation a stairway. The stairway should be described by the number of stones in the initial coordinate and the coordinates of the stairway's beginning and end. Each following cell in the coordinate's increasing order should contain one cubical stone more than the previous one. At that if the cell has already got stones, they do not count in this building process, the stairways were simply built on them. In other words, let us assume that a stairway is built with the initial coordinate of l , the final coordinate of r and the number of stones in the initial coordinate x . That means that x stones will be added in the cell l , x ΓÇë+ΓÇë1 stones will be added in the cell l ΓÇë+ΓÇë1 , ..., x ΓÇë+ΓÇë r ΓÇë-ΓÇë l stones will be added in the cell r .

Chris managed to find an ancient manuscript, containing the descriptions of all the stairways. Now he wants to compare the data to be sure that he has really found "A Road to the Sun". For that he chose some road cells and counted the total number of cubical stones that has been accumulated throughout the Martian history and then asked you to count using the manuscript to what the sum should ideally total.

## Input

The first line contains three space-separated integers: n ,ΓÇë m ,ΓÇë k ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë10 5 ,ΓÇë1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë min ( n ,ΓÇë100) ) which is the number of cells, the number of "Roads to the Sun" and the number of cells in the query correspondingly. Each of the following m roads contain three space-separated integers: a i ,ΓÇë b i ,ΓÇë c i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë b i ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë1000 ) which are the stairway's description, its beginning, end and the initial cell's height. Then follow a line, containing k different space-separated integers b i . All these numbers ranging from 1 to n are cells, the number of stones in which interests Chris.

## Output

You have to print a single number on a single line which is the sum of stones in all the cells Chris is interested in.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d ).

## Examples

Example 1:
```
5 2 1
1 5 1
2 4 1
3
```
```
5
```
