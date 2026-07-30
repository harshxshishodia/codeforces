# D. Two out of Three

**Submission:** https://codeforces.com/contest/82/problem/D

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

Vasya has recently developed a new algorithm to optimize the reception of customer flow and he considered the following problem.

Let the queue to the cashier contain n people, at that each of them is characterized by a positive integer a i ΓÇö that is the time needed to work with this customer. What is special about this very cashier is that it can serve two customers simultaneously. However, if two customers need a i and a j of time to be served, the time needed to work with both of them customers is equal to max ( a i ,ΓÇë a j ) . Please note that working with customers is an uninterruptable process, and therefore, if two people simultaneously come to the cashier, it means that they begin to be served simultaneously, and will both finish simultaneously (it is possible that one of them will have to wait).

Vasya used in his algorithm an ingenious heuristic ΓÇö as long as the queue has more than one person waiting, then some two people of the first three standing in front of the queue are sent simultaneously . If the queue has only one customer number i , then he goes to the cashier, and is served within a i of time. Note that the total number of phases of serving a customer will always be equal to Γîê n ΓÇë/ΓÇë2Γîë .

Vasya thinks that this method will help to cope with the queues we all hate. That's why he asked you to work out a program that will determine the minimum time during which the whole queue will be served using this algorithm.

## Input

The first line of the input file contains a single number n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë1000 ), which is the number of people in the sequence. The second line contains space-separated integers a 1 ,ΓÇë a 2 ,ΓÇë...,ΓÇë a n ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 6 ). The people are numbered starting from the cashier to the end of the queue.

## Output

Print on the first line a single number ΓÇö the minimum time needed to process all n people. Then on Γîê n ΓÇë/ΓÇë2Γîë lines print the order in which customers will be served. Each line (probably, except for the last one) must contain two numbers separated by a space ΓÇö the numbers of customers who will be served at the current stage of processing. If n is odd, then the last line must contain a single number ΓÇö the number of the last served customer in the queue. The customers are numbered starting from 1 .

## Examples

Example 1:
```
4
1 2 3 4
```
```
6
1 2
3 4
```
