# B. Colorful Field

**Submission:** https://codeforces.com/contest/79/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Fox Ciel saw a large field while she was on a bus. The field was a n ΓÇë├ùΓÇë m rectangle divided into 1ΓÇë├ùΓÇë1 cells. Some cells were wasteland, and other each cell contained crop plants: either carrots or kiwis or grapes. 

After seeing the field carefully, Ciel found that the crop plants of each cell were planted in following procedure:

 
- Assume that the rows are numbered 1 to n from top to bottom and the columns are numbered 1 to m from left to right, and a cell in row i and column j is represented as ( i ,ΓÇë j ) . 
- First, each field is either cultivated or waste. Crop plants will be planted in the cultivated cells in the order of (1,ΓÇë1)ΓÇëΓåÆΓÇë...ΓÇëΓåÆΓÇë(1,ΓÇë m )ΓÇëΓåÆΓÇë(2,ΓÇë1)ΓÇëΓåÆΓÇë...ΓÇëΓåÆΓÇë(2,ΓÇë m )ΓÇëΓåÆΓÇë...ΓÇëΓåÆΓÇë( n ,ΓÇë1)ΓÇëΓåÆΓÇë...ΓÇëΓåÆΓÇë( n ,ΓÇë m ) . Waste cells will be ignored. 
- Crop plants (either carrots or kiwis or grapes) will be planted in each cell one after another cyclically. Carrots will be planted in the first cell, then kiwis in the second one, grapes in the third one, carrots in the forth one, kiwis in the fifth one, and so on. 

The following figure will show you the example of this procedure. Here, a white square represents a cultivated cell, and a black square represents a waste cell.
 
Now she is wondering how to determine the crop plants in some certain cells.

## Input

In the first line there are four positive integers n ,ΓÇë m ,ΓÇë k ,ΓÇë t ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë4┬╖10 4 ,ΓÇë1ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë4┬╖10 4 ,ΓÇë1ΓÇëΓëñΓÇë k ΓÇëΓëñΓÇë10 3 ,ΓÇë1ΓÇëΓëñΓÇë t ΓÇëΓëñΓÇë10 3 ), each of which represents the height of the field, the width of the field, the number of waste cells and the number of queries that ask the kind of crop plants in a certain cell.

Following each k lines contains two integers a ,ΓÇë b ( 1ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë m ), which denotes a cell ( a ,ΓÇë b ) is waste. It is guaranteed that the same cell will not appear twice in this section.

Following each t lines contains two integers i ,ΓÇë j ( 1ΓÇëΓëñΓÇë i ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë j ΓÇëΓëñΓÇë m ), which is a query that asks you the kind of crop plants of a cell ( i ,ΓÇë j ) .

## Output

For each query, if the cell is waste, print Waste . Otherwise, print the name of crop plants in the cell: either Carrots or Kiwis or Grapes .

## Examples

Example 1:
```
4 5 5 6
4 3
1 3
3 3
2 5
3 2
1 3
1 4
2 3
2 4
1 1
1 1
```
```
Waste
Grapes
Carrots
Kiwis
Carrots
Carrots
```

## Note

The sample corresponds to the figure in the statement.
