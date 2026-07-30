# E. Mushroom Gnomes

**Submission:** https://codeforces.com/contest/60/problem/E

**Limits:** 3 seconds / 256 megabytes

## Problem Statement

Once upon a time in the thicket of the mushroom forest lived mushroom gnomes. They were famous among their neighbors for their magic mushrooms. Their magic nature made it possible that between every two neighboring mushrooms every minute grew another mushroom with the weight equal to the sum of weights of two neighboring ones. 

The mushroom gnomes loved it when everything was in order, that's why they always planted the mushrooms in one line in the order of their weights' increasing. Well... The gnomes planted the mushrooms and went to eat. After x minutes they returned and saw that new mushrooms had grown up, so that the increasing order had been violated. The gnomes replanted all the mushrooms in the correct order, that is, they sorted the mushrooms in the order of the weights' increasing. And went to eat again (those gnomes were quite big eaters). What total weights modulo p will the mushrooms have in another y minutes?

## Input

The first line contains four integers n , x , y , p ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 6 ,ΓÇë0ΓÇëΓëñΓÇë x ,ΓÇë y ΓÇëΓëñΓÇë10 18 ,ΓÇë x ΓÇë+ΓÇë y ΓÇë>ΓÇë0,ΓÇë2ΓÇëΓëñΓÇë p ΓÇëΓëñΓÇë10 9 ) which represent the number of mushrooms, the number of minutes after the first replanting, the number of minutes after the second replanting and the module. The next line contains n integers a i which represent the mushrooms' weight in the non-decreasing order ( 0ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë10 9 ).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d ).

## Output

The answer should contain a single number which is the total weights of the mushrooms modulo p in the end after x ΓÇë+ΓÇë y minutes.

## Examples

Example 1:
```
2 1 0 657276545
1 2
```
```
6
```
