# C. Corporation Mail

**Submission:** https://codeforces.com/contest/56/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

The Beroil corporation structure is hierarchical, that is it can be represented as a tree. Let's examine the presentation of this structure as follows:

 
- employee ::= name . | name : employee 1 , employee 2 , ... , employee k . 
- name ::= name of an employee 

That is, the description of each employee consists of his name, a colon ( : ), the descriptions of all his subordinates separated by commas, and, finally, a dot. If an employee has no subordinates, then the colon is not present in his description.

For example, line MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY... is the correct way of recording the structure of a corporation where the director MIKE has subordinates MAX , ARTEM and DMITRY . ARTEM has a subordinate whose name is MIKE , just as the name of his boss and two subordinates of DMITRY are called DMITRY , just like himself.

In the Beroil corporation every employee can only correspond with his subordinates, at that the subordinates are not necessarily direct. Let's call an uncomfortable situation the situation when a person whose name is s writes a letter to another person whose name is also s . In the example given above are two such pairs: a pair involving MIKE , and two pairs for DMITRY (a pair for each of his subordinates).

Your task is by the given structure of the corporation to find the number of uncomfortable pairs in it.

## Input

The first and single line contains the corporation structure which is a string of length from 1 to 1000 characters. It is guaranteed that the description is correct. Every name is a string consisting of capital Latin letters from 1 to 10 symbols in length.

## Output

Print a single number ΓÇö the number of uncomfortable situations in the company.

## Examples

Example 1:
```
MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY...
```
```
3
```
