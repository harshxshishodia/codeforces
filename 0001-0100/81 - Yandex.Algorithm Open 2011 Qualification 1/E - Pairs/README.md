# E. Pairs

**Submission:** https://codeforces.com/contest/81/problem/E

**Limits:** 1 second / 256 megabytes

## Problem Statement

There are n students in Polycarp's class (including himself). A few days ago all students wrote an essay "My best friend". Each student's essay was dedicated to one of the students of class, to his/her best friend. Note that student b 's best friend is not necessarily student a , if a 's best friend is b .

And now the teacher leads the whole class to the museum of the history of sports programming. Exciting stories of legendary heroes await the students: tourist, Petr, tomek, SnapDragon ΓÇö that's who they will hear about!

The teacher decided to divide students into pairs so that each pair consisted of a student and his best friend. She may not be able to split all the students into pairs, it's not a problem ΓÇö she wants to pick out the maximum number of such pairs. If there is more than one variant of doing so, she wants to pick out the pairs so that there were as much boy-girl pairs as possible. Of course, each student must not be included in more than one pair.

## Input

The first line contains an integer n ( 2ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ), n is the number of students per class. Next, n lines contain information about the students, one per line. Each line contains two integers f i ,ΓÇë s i ( 1ΓÇëΓëñΓÇë f i ΓÇëΓëñΓÇë n ,ΓÇë f i ΓÇëΓëáΓÇë i ,ΓÇë1ΓÇëΓëñΓÇë s i ΓÇëΓëñΓÇë2 ), where f i is the number of i -th student's best friend and s i denotes the i -th pupil's sex ( s i ΓÇë=ΓÇë1 for a boy and s i ΓÇë=ΓÇë2 for a girl).

## Output

Print on the first line two numbers t , e , where t is the maximum number of formed pairs, and e is the maximum number of boy-girl type pairs among them. Then print t lines, each line must contain a pair a i ,ΓÇë b i ( 1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë n ), they are numbers of pupils in the i -th pair. Print the pairs in any order. Print the numbers in pairs in any order. If there are several solutions, output any of them.

## Examples

Example 1:
```
5
5 2
3 2
5 1
2 1
4 2
```
```
2 2
5 3
4 2
```

## Note

The picture corresponds to the first sample. On the picture rhomb stand for boys, squares stand for girls, arrows lead from a pupil to his/her best friend. Bold non-dashed arrows stand for pairs in the answer.
