# C. General Mobilization

**Submission:** https://codeforces.com/contest/82/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

The Berland Kingdom is a set of n cities connected with each other with n ΓÇë-ΓÇë1 railways. Each road connects exactly two different cities. The capital is located in city 1 . For each city there is a way to get from there to the capital by rail.

In the i -th city there is a soldier division number i , each division is characterized by a number of a i . It represents the priority, the smaller the number, the higher the priority of this division. All values of a i are different.

One day the Berland King Berl Great declared a general mobilization, and for that, each division should arrive in the capital. Every day from every city except the capital a train departs. So there are exactly n ΓÇë-ΓÇë1 departing trains each day. Each train moves toward the capital and finishes movement on the opposite endpoint of the railway on the next day. It has some finite capacity of c j , expressed in the maximum number of divisions, which this train can transport in one go. Each train moves in the direction of reducing the distance to the capital. So each train passes exactly one railway moving from a city to the neighboring (where it stops) toward the capital.

In the first place among the divisions that are in the city, division with the smallest number of a i get on the train, then with the next smallest and so on, until either the train is full or all the divisions are be loaded. So it is possible for a division to stay in a city for a several days.

The duration of train's progress from one city to another is always equal to 1 day. All divisions start moving at the same time and end up in the capital, from where they don't go anywhere else any more. Each division moves along a simple path from its city to the capital, regardless of how much time this journey will take.

Your goal is to find for each division, in how many days it will arrive to the capital of Berland. The countdown begins from day 0 .

## Input

The first line contains the single integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë5000 ). It is the number of cities in Berland. The second line contains n space-separated integers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n , where a i represents the priority of the division, located in the city number i . All numbers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n are different ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ). Then n ΓÇë-ΓÇë1 lines contain the descriptions of the railway roads. Each description consists of three integers v j ,ΓÇë u j ,ΓÇë c j , where v j , u j are number of cities connected by the j -th rail, and c j stands for the maximum capacity of a train riding on this road ( 1ΓÇëΓëñΓÇë v j ,ΓÇë u j ΓÇëΓëñΓÇë n ,ΓÇë v j ΓÇëΓëáΓÇë u j , 1ΓÇëΓëñΓÇë c j ΓÇëΓëñΓÇë n ).

## Output

Print sequence t 1 ,ΓÇë t 2 ,ΓÇë...,ΓÇë t n , where t i stands for the number of days it takes for the division of city i to arrive to the capital. Separate numbers with spaces.

## Examples

Example 1:
```
4
40 10 30 20
1 2 1
2 3 1
4 2 1
```
```
0 1 3 2
```
