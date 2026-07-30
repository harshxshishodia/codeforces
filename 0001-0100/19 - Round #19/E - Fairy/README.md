# E. Fairy

**Submission:** https://codeforces.com/contest/19/problem/E

**Limits:** 1.5 seconds / 256 megabytes

## Problem Statement

Once upon a time there lived a good fairy A. One day a fine young man B came to her and asked to predict his future. The fairy looked into her magic ball and said that soon the fine young man will meet the most beautiful princess ever and will marry her. Then she drew on a sheet of paper n points and joined some of them with segments, each of the segments starts in some point and ends in some other point. Having drawn that picture, she asked the young man to erase one of the segments from the sheet. Then she tries to colour each point red or blue so, that there is no segment having points of the same colour as its ends. If she manages to do so, the prediction will come true. B wants to meet the most beautiful princess, that's why he asks you to help him. Find all the segments that will help him to meet the princess.

## Input

The first input line contains two integer numbers: n ΓÇö amount of the drawn points and m ΓÇö amount of the drawn segments ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 4 ,ΓÇë0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10 4 ). The following m lines contain the descriptions of the segments. Each description contains two different space-separated integer numbers v , u ( 1ΓÇëΓëñΓÇë v ΓÇëΓëñΓÇë n ,ΓÇë1ΓÇëΓëñΓÇë u ΓÇëΓëñΓÇë n ) ΓÇö indexes of the points, joined by this segment. No segment is met in the description twice.

## Output

In the first line output number k ΓÇö amount of the segments in the answer. In the second line output k space-separated numbers ΓÇö indexes of these segments in ascending order. Each index should be output only once. Segments are numbered from 1 in the input order.

## Examples

Example 1:
```
4 4
1 2
1 3
2 4
3 4
```
```
4
1 2 3 4
```
