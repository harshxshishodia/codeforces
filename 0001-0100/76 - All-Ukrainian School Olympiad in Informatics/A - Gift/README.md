# A. Gift

**Submission:** https://codeforces.com/contest/76/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

The kingdom of Olympia consists of N cities and M bidirectional roads. Each road connects exactly two cities and two cities can be connected with more than one road. Also it possible that some roads connect city with itself making a loop.

All roads are constantly plundered with bandits. After a while bandits became bored of wasting time in road robberies, so they suggested the king of Olympia to pay off. According to the offer, bandits want to get a gift consisted of gold and silver coins. Offer also contains a list of restrictions: for each road it is known g i ΓÇö the smallest amount of gold and s i ΓÇö the smallest amount of silver coins that should be in the gift to stop robberies on the road. That is, if the gift contains a gold and b silver coins, then bandits will stop robberies on all the roads that g i ΓÇëΓëñΓÇë a and s i ΓÇëΓëñΓÇë b .

Unfortunately kingdom treasury doesn't contain neither gold nor silver coins, but there are Olympian tugriks in it. The cost of one gold coin in tugriks is G , and the cost of one silver coin in tugriks is S . King really wants to send bandits such gift that for any two cities there will exist a safe path between them. Your task is to find the minimal cost in Olympian tugriks of the required gift.

## Input

The first line of the input contains two integers N and M ( 2ΓÇëΓëñΓÇë N ΓÇëΓëñΓÇë200 , 1ΓÇëΓëñΓÇë M ΓÇëΓëñΓÇë50ΓÇë000 ) ΓÇö the number of cities and the number of roads, respectively. The second line contains two integers G and S ( 1ΓÇëΓëñΓÇë G ,ΓÇë S ΓÇëΓëñΓÇë10 9 ) ΓÇö the prices of gold and silver coins in tugriks. The following M lines contain information about the offer. Each of the records in list is given as four integers x i ,ΓÇë y i ,ΓÇë g i ,ΓÇë s i , where x i and y i are the numbers of cities that the road connects and g i , s i are minimal gold and silver coins requirements for the i -th road ( 1ΓÇëΓëñΓÇë x i ,ΓÇë y i ΓÇëΓëñΓÇë N , 1ΓÇëΓëñΓÇë g i ,ΓÇë s i ΓÇëΓëñΓÇë10 9 ). Cities are numbered from 1 to N . It is possible that there are more than one road between a pair of cities. It is possible that a road connects the city with itself.

## Output

The output should contain the minimal cost of the gift in Olympian tugriks. If there is no gift that satisfies the given requirements output .

## Examples

Example 1:
```
3 3
2 1
1 2 10 15
1 2 4 20
1 3 5 1
```
```
30
```
