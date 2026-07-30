# C. Synchrophasotron

**Submission:** https://codeforces.com/contest/68/problem/C

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

For some experiments little Petya needs a synchrophasotron. He has already got the device, all that's left is to set the fuel supply. Fuel comes through a system of nodes numbered from 1 to n and connected by pipes. Pipes go from every node with smaller number to every node with greater number. Fuel can only flow through pipes in direction from node with smaller number to node with greater number. Any amount of fuel can enter through the first node and the last node is connected directly to the synchrophasotron. It is known that every pipe has three attributes: the minimum amount of fuel that should go through it, the maximum amount of fuel that can possibly go through it and the cost of pipe activation. If c ij units of fuel ( c ij ΓÇë>ΓÇë0 ) flow from node i to node j , it will cost a ij ΓÇë+ΓÇë c ij 2 tugriks ( a ij is the cost of pipe activation), and if fuel doesn't flow through the pipe, it doesn't cost anything. Only integer number of units of fuel can flow through each pipe.

Constraints on the minimal and the maximal fuel capacity of a pipe take place always , not only if it is active. You may assume that the pipe is active if and only if the flow through it is strictly greater than zero.

Petya doesn't want the pipe system to be overloaded, so he wants to find the minimal amount of fuel, that, having entered the first node, can reach the synchrophasotron. Besides that he wants to impress the sponsors, so the sum of money needed to be paid for fuel to go through each pipe, must be as big as possible.

## Input

First line contains integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë6 ), which represents the number of nodes. Each of the next n ( n ΓÇë-ΓÇë1)ΓÇë/ΓÇë2 lines contains five integers s ,ΓÇë f ,ΓÇë l ,ΓÇë h ,ΓÇë a that describe pipes ΓÇö the first node of the pipe, the second node of the pipe, the minimum and the maximum amount of fuel that can flow through the pipe and the the activation cost, respectively. ( 1ΓÇëΓëñΓÇë s ΓÇë<ΓÇë f ΓÇëΓëñΓÇë n ,ΓÇë0ΓÇëΓëñΓÇë l ΓÇëΓëñΓÇë h ΓÇëΓëñΓÇë5,ΓÇë0ΓÇëΓëñΓÇë a ΓÇëΓëñΓÇë6 ). It is guaranteed that for each pair of nodes with distinct numbers there will be exactly one pipe between them described in the input.

## Output

Output in the first line two space-separated numbers: the minimum possible amount of fuel that can flow into the synchrophasotron, and the maximum possible sum that needs to be paid in order for that amount of fuel to reach synchrophasotron. If there is no amount of fuel that can reach synchrophasotron, output " -1 -1 ".

The amount of fuel which will flow into synchrophasotron is not neccessary positive. It could be equal to zero if the minimum constraint of every pipe is equal to zero.

## Examples

Example 1:
```
2
1 2 1 2 3
```
```
1 4
```

## Note

In the first test, we can either pass 1 or 2 units of fuel from node 1 to node 2. The minimum possible amount is 1, it costs a 12 ΓÇë+ΓÇë1 2 ΓÇë=ΓÇë4 .

In the second test, you can pass at most 2 units from node 1 to node 2, and at you have to pass at least 3 units from node 2 to node 3. It is impossible.

In the third test, the minimum possible amount is 2. You can pass each unit of fuel through two different paths: either 1->2->3->4 or 1->3->4. If you use the first path twice, it will cost a 12 ΓÇë+ΓÇë2 2 ΓÇë+ΓÇë a 23 ΓÇë+ΓÇë2 2 ΓÇë+ΓÇë a 34 ΓÇë+ΓÇë2 2 =14. If you use the second path twice, it will cost a 13 ΓÇë+ΓÇë2 2 ΓÇë+ΓÇë a 34 ΓÇë+ΓÇë2 2 =14. However, if you use each path (allowing one unit of fuel go through pipes 1->2, 2->3, 1->3, and two units go through 3->4) it will cost a 12 ΓÇë+ΓÇë1 2 ΓÇë+ΓÇë a 23 ΓÇë+ΓÇë1 2 ΓÇë+ΓÇë a 13 ΓÇë+ΓÇë1 2 ΓÇë+ΓÇë a 34 ΓÇë+ΓÇë2 2 =15 and it is the maximum possible cost.

Also note that since no fuel flows from node 1 to node 4, activation cost for that pipe is not added to the answer.
