# C. Average Score

**Submission:** https://codeforces.com/contest/81/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

After the educational reform Polycarp studies only two subjects at school, Safety Studies and PE (Physical Education). During the long months of the fourth term, he received n marks in them. When teachers wrote a mark in the journal, they didn't write in what subject the mark was for, they just wrote the mark.

Now it's time to show the journal to his strict parents. Polycarp knows that recently at the Parent Meeting the parents were told that he received a Safety Studies marks and b PE marks ( a ΓÇë+ΓÇë b ΓÇë=ΓÇë n ). Now Polycarp wants to write a subject's name in front of each mark so that: 

 
- there are exactly a Safety Studies marks, 
- there are exactly b PE marks, 
- the total average score in both subjects is maximum. 

An average subject grade is the sum of all marks in it, divided by the number of them. Of course, the division is performed in real numbers without rounding up or down. Polycarp aims to maximize the x 1 ΓÇë+ΓÇë x 2 , where x 1 is the average score in the first subject (Safety Studies), and x 2 is the average score in the second one (Physical Education).

## Input

The first line contains an integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ), n is the number of marks in Polycarp's Journal. The second line contains two positive integers a ,ΓÇë b ( 1ΓÇëΓëñΓÇë a ,ΓÇë b ΓÇëΓëñΓÇë n ΓÇë-ΓÇë1,ΓÇë a ΓÇë+ΓÇë b ΓÇë=ΓÇë n ). The third line contains a sequence of integers t 1 ,ΓÇë t 2 ,ΓÇë...,ΓÇë t n ( 1ΓÇëΓëñΓÇë t i ΓÇëΓëñΓÇë5 ), they are Polycarp's marks.

## Output

Print the sequence of integers f 1 ,ΓÇë f 2 ,ΓÇë...,ΓÇë f n , where f i ( 1ΓÇëΓëñΓÇë f i ΓÇëΓëñΓÇë2 ) is the number of a subject to which the i -th mark should be attributed. If there are several possible solutions, then print such that the sequence f 1 ,ΓÇë f 2 ,ΓÇë...,ΓÇë f n is the smallest lexicographically.

The sequence p 1 ,ΓÇë p 2 ,ΓÇë...,ΓÇë p n is lexicographically less than q 1 ,ΓÇë q 2 ,ΓÇë...,ΓÇë q n if there exists such j ( 1ΓÇëΓëñΓÇë j ΓÇëΓëñΓÇë n ) that p i ΓÇë=ΓÇë q i for all 1ΓÇëΓëñΓÇë i ΓÇë<ΓÇë j , ╨░nd p j ΓÇë<ΓÇë q j .

## Examples

Example 1:
```
5
3 2
4 4 5 4 4
```
```
1 1 2 1 2
```

## Note

In the first sample the average score in the first subject is equal to 4, and in the second one ΓÇö to 4.5. The total average score is 8.5.
