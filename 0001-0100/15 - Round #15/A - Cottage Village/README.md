# A. Cottage Village

**Submission:** https://codeforces.com/contest/15/problem/A

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

A new cottage village called ┬½Flatville┬╗ is being built in Flatland. By now they have already built in ┬½Flatville┬╗ n square houses with the centres on the ╨₧x -axis. The houses' sides are parallel to the coordinate axes. It's known that no two houses overlap, but they can touch each other.

The architect bureau, where Peter works, was commissioned to build a new house in ┬½Flatville┬╗. The customer wants his future house to be on the ╨₧x -axis, to be square in shape, have a side t , and touch at least one of the already built houses. For sure, its sides should be parallel to the coordinate axes, its centre should be on the Ox -axis and it shouldn't overlap any of the houses in the village.

Peter was given a list of all the houses in ┬½Flatville┬╗. Would you help him find the amount of possible positions of the new house?

## Input

The first line of the input data contains numbers n and t ( 1ΓÇëΓëñΓÇë n ,ΓÇë t ΓÇëΓëñΓÇë1000 ). Then there follow n lines, each of them contains two space-separated integer numbers: x i a i , where x i ΓÇö x -coordinate of the centre of the i -th house, and a i ΓÇö length of its side ( ΓÇë-ΓÇë1000ΓÇëΓëñΓÇë x i ΓÇëΓëñΓÇë1000 , 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë1000 ).

## Output

Output the amount of possible positions of the new house.

## Examples

Example 1:
```
2 2
0 4
6 2
```
```
4
```

## Note

It is possible for the x -coordinate of the new house to have non-integer value.
