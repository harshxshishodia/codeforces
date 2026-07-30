# B. Embassy Queue

**Submission:** https://codeforces.com/contest/85/problem/B

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

In an embassy of a well-known kingdom an electronic queue is organised. Every person who comes to the embassy, needs to make the following three actions: show the ID, pay money to the cashier and be fingerprinted. Besides, the actions should be performed in the given order. 

For each action several separate windows are singled out: k 1 separate windows for the first action (the first type windows), k 2 windows for the second one (the second type windows), and k 3 for the third one (the third type windows). The service time for one person in any of the first type window equals to t 1 . Similarly, it takes t 2 time to serve a person in any of the second type windows. And it takes t 3 to serve one person in any of the third type windows. Thus, the service time depends only on the window type and is independent from the person who is applying for visa.

At some moment n people come to the embassy, the i -th person comes at the moment of time c i . The person is registered under some number. After that he sits in the hall and waits for his number to be shown on a special board. Besides the person's number the board shows the number of the window where one should go and the person goes there immediately. Let's consider that the time needed to approach the window is negligible. The table can show information for no more than one person at a time. The electronic queue works so as to immediately start working with the person who has approached the window, as there are no other people in front of the window.

The Client Service Quality inspectors noticed that several people spend too much time in the embassy (this is particularly tiresome as the embassy has no mobile phone reception and 3G). It was decided to organise the system so that the largest time a person spends in the embassy were minimum. Help the inspectors organise the queue. Consider that all actions except for being served in at the window, happen instantly.

## Input

The first line contains three space-separated integers k 1 , k 2 , k 3 ( 1ΓÇëΓëñΓÇë k i ΓÇëΓëñΓÇë10 9 ), they are the number of windows of the first, second and third type correspondingly.

The second line contains three space-separated integers t 1 , t 2 , t 3 ( 1ΓÇëΓëñΓÇë t i ΓÇëΓëñΓÇë10 5 ), they are the periods of time needed to serve one person in the window of the first, second and third type correspondingly. 

The third line contains an integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ), it is the number of people.

The fourth line contains n space-separated integers c i ( 1ΓÇëΓëñΓÇë c i ΓÇëΓëñΓÇë10 9 ) in the non-decreasing order; c i is the time when the person number i comes to the embassy.

## Output

Print the single number, the maximum time a person will spend in the embassy if the queue is organized optimally.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin , cout streams (also you may use the %I64d specificator).

## Examples

Example 1:
```
1 1 1
1 1 1
5
1 1 1 1 1
```
```
7
```

## Note

In the first test 5 people come simultaneously at the moment of time equal to 1. There is one window of every type, it takes 1 unit of time to be served at each window. That's why the maximal time a person spends in the embassy is the time needed to be served at the windows (3 units of time) plus the time the last person who comes to the first window waits (4 units of time).

 Windows in the second test work like this:

The first window of the first type: [1,ΓÇë6) ΓÇö the first person, [6,ΓÇë11) ΓÇö third person, [11,ΓÇë16) ΓÇö fifth person

The second window of the first type: [2,ΓÇë7) ΓÇö the second person, [7,ΓÇë12) ΓÇö the fourth person

The only second type window: [6,ΓÇë7) ΓÇö first, [7,ΓÇë8) ΓÇö second, [11,ΓÇë12) ΓÇö third, [12,ΓÇë13) ΓÇö fourth, [16,ΓÇë17) ΓÇö fifth

The only third type window: [7,ΓÇë8) ΓÇö first, [8,ΓÇë9) ΓÇö second, [12,ΓÇë13) ΓÇö third, [13,ΓÇë14) ΓÇö fourth, [17,ΓÇë18) ΓÇö fifth

We can see that it takes most time to serve the fifth person.
