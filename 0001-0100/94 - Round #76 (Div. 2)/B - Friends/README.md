# B. Friends

**Submission:** https://codeforces.com/contest/94/problem/B

**Limits:** 1 second / 256 megabytes

## Problem Statement

One day Igor K. stopped programming and took up math. One late autumn evening he was sitting at a table reading a book and thinking about something. 

The following statement caught his attention: "Among any six people there are either three pairwise acquainted people or three pairwise unacquainted people"

Igor just couldn't get why the required minimum is 6 people. "Well, that's the same for five people, too!" ΓÇö he kept on repeating in his mind. ΓÇö "Let's take, say, Max, Ilya, Vova ΓÇö here, they all know each other! And now let's add Dima and Oleg to Vova ΓÇö none of them is acquainted with each other! Now, that math is just rubbish!"

Igor K. took 5 friends of his and wrote down who of them is friends with whom. Now he wants to check whether it is true for the five people that among them there are either three pairwise acquainted or three pairwise not acquainted people.

## Input

The first line contains an integer m (0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10) , which is the number of relations of acquaintances among the five friends of Igor's.

Each of the following m lines contains two integers a i and b i (1ΓÇëΓëñΓÇë a i ,ΓÇë b i ΓÇëΓëñΓÇë5; a i ΓÇëΓëáΓÇë b i ) , where ( a i ,ΓÇë b i ) is a pair of acquainted people. It is guaranteed that each pair of the acquaintances is described exactly once. The acquaintance relation is symmetrical, i.e. if x is acquainted with y , then y is also acquainted with x .

## Output

Print " FAIL ", if among those five people there are no either three pairwise acquainted or three pairwise unacquainted people. Otherwise print " WIN ".

## Examples

Example 1:
```
4
1 3
2 3
1 4
5 3
```
```
WIN
```
