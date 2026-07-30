# E. Number Table

**Submission:** https://codeforces.com/contest/40/problem/E

**Limits:** 2 seconds / 216 megabytes

## Problem Statement

As it has been found out recently, all the Berland's current economical state can be described using a simple table n ΓÇë├ùΓÇë m in size. n ΓÇö the number of days in each Berland month, m ΓÇö the number of months. Thus, a table cell corresponds to a day and a month of the Berland's year. Each cell will contain either 1 , or -1 , which means the state's gains in a particular month, on a particular day. 1 corresponds to profits, -1 corresponds to losses. It turned out important for successful development to analyze the data on the state of the economy of the previous year, however when the treasurers referred to the archives to retrieve the data, it turned out that the table had been substantially damaged. In some table cells the number values had faded and were impossible to be deciphered. It is known that the number of cells in which the data had been preserved is strictly less than max ( n ,ΓÇë m ) . However, there is additional information ΓÇö the product of the numbers in each line and column equaled -1 . Your task is to find out how many different tables may conform to the preserved data. As the answer to the task can be quite large, you have to find it modulo p .

## Input

The first line contains integers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë1000 ). The second line contains the integer k ( 0ΓÇëΓëñΓÇë k ΓÇë<ΓÇë max ( n ,ΓÇë m ) ) ΓÇö the number of cells in which the data had been preserved. The next k lines contain the data on the state of the table in the preserved cells. Each line is of the form " a b c ", where a ( 1ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë n ) ΓÇö the number of the table row, b ( 1ΓÇëΓëñΓÇë b ΓÇëΓëñΓÇë m ) ΓÇö the number of the column, c ΓÇö the value containing in the cell ( 1 or -1 ). They are numbered starting from 1 . It is guaranteed that no two lines with same a and b values exist. The last line contains an integer p ( 2ΓÇëΓëñΓÇë p ΓÇëΓëñΓÇë10 9 ΓÇë+ΓÇë7 ).

## Output

Print the number of different tables that could conform to the preserved data modulo p .

## Examples

Example 1:
```
2 2
0
100
```
```
2
```
