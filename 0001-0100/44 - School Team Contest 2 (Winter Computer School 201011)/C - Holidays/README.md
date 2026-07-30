# C. Holidays

**Submission:** https://codeforces.com/contest/44/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

School holidays come in Berland. The holidays are going to continue for n days. The students of school Γäû N are having the time of their lives and the IT teacher Marina Sergeyevna, who has spent all the summer busy checking the BSE (Berland State Examination) results, has finally taken a vacation break! Some people are in charge of the daily watering of flowers in shifts according to the schedule. However when Marina Sergeyevna was making the schedule, she was so tired from work and so lost in dreams of the oncoming vacation that she perhaps made several mistakes. In fact, it is possible that according to the schedule, on some days during the holidays the flowers will not be watered or will be watered multiple times. Help Marina Sergeyevna to find a mistake.

## Input

The first input line contains two numbers n and m ( 1ΓÇëΓëñΓÇë n ,ΓÇë m ΓÇëΓëñΓÇë100 ) ΓÇö the number of days in Berland holidays and the number of people in charge of the watering respectively. The next m lines contain the description of the duty schedule. Each line contains two integers a i and b i ( 1ΓÇëΓëñΓÇë a i ΓÇëΓëñΓÇë b i ΓÇëΓëñΓÇë n ), meaning that the i -th person in charge should water the flowers from the a i -th to the b i -th day inclusively, once a day. The duty shifts are described sequentially, i.e. b i ΓÇëΓëñΓÇë a i ΓÇë+ΓÇë1 for all i from 1 to n ΓÇë-ΓÇë1 inclusively.

## Output

Print "OK" (without quotes), if the schedule does not contain mistakes. Otherwise you have to find the minimal number of a day when the flowers will not be watered or will be watered multiple times, and output two integers ΓÇö the day number and the number of times the flowers will be watered that day.

## Examples

Example 1:
```
10 5
1 2
3 3
4 6
7 7
8 10
```
```
OK
```

## Note

Keep in mind that in the second sample the mistake occurs not only on the second day, but also on the sixth day, when nobody waters the flowers. However, you have to print the second day, i.e. the day with the minimal number.
