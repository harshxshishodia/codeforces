# D. Don't fear, DravDe is kind

**Submission:** https://codeforces.com/contest/28/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

A motorcade of n trucks, driving from city ┬½Z┬╗ to city ┬½╨ù┬╗, has approached a tunnel, known as Tunnel of Horror. Among truck drivers there were rumours about monster DravDe, who hunts for drivers in that tunnel. Some drivers fear to go first, others - to be the last, but let's consider the general case. Each truck is described with four numbers: 

 
- v ΓÇö value of the truck, of its passangers and cargo 
- c ΓÇö amount of passanger on the truck, the driver included 
- l ΓÇö total amount of people that should go into the tunnel before this truck, so that the driver can overcome his fear (┬½if the monster appears in front of the motorcade, he'll eat them first┬╗) 
- r ΓÇö total amount of people that should follow this truck, so that the driver can overcome his fear (┬½if the monster appears behind the motorcade, he'll eat them first┬╗). 

Since the road is narrow, it's impossible to escape DravDe, if he appears from one side. Moreover, the motorcade can't be rearranged. The order of the trucks can't be changed, but it's possible to take any truck out of the motorcade, and leave it near the tunnel for an indefinite period. You, as the head of the motorcade, should remove some of the trucks so, that the rest of the motorcade can move into the tunnel and the total amount of the left trucks' values is maximal.

## Input

The first input line contains integer number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö amount of trucks in the motorcade. The following n lines contain four integers each. Numbers in the i -th line: v i ,ΓÇë c i ,ΓÇë l i ,ΓÇë r i ( 1ΓÇëΓëñΓÇë v i ΓÇëΓëñΓÇë10 4 ,ΓÇë1ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë10 5 ,ΓÇë0ΓÇëΓëñΓÇë l i ,ΓÇë r i ΓÇëΓëñΓÇë10 5 ) ΓÇö describe the i -th truck. The trucks are numbered from 1, counting from the front of the motorcade.

## Output

In the first line output number k ΓÇö amount of trucks that will drive into the tunnel. In the second line output k numbers ΓÇö indexes of these trucks in ascending order. Don't forget please that you are not allowed to change the order of trucks. If the answer is not unique, output any.

## Examples

Example 1:
```
5
1 1 0 3
1 1 1 2
1 1 2 1
1 1 3 0
2 1 3 0
```
```
4
1 2 3 5
```
