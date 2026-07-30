# C. Mail Stamps

**Submission:** https://codeforces.com/contest/29/problem/C

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

One day Bob got a letter in an envelope. Bob knows that when Berland's post officers send a letter directly from city ┬½A┬╗ to city ┬½B┬╗ , they stamp it with ┬½A B┬╗ , or ┬½B A┬╗ . Unfortunately, often it is impossible to send a letter directly from the city of the sender to the city of the receiver, that's why the letter is sent via some intermediate cities. Post officers never send a letter in such a way that the route of this letter contains some city more than once. Bob is sure that the post officers stamp the letters accurately.

There are n stamps on the envelope of Bob's letter. He understands that the possible routes of this letter are only two. But the stamps are numerous, and Bob can't determine himself none of these routes. That's why he asks you to help him. Find one of the possible routes of the letter.

## Input

The first line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ) ΓÇö amount of mail stamps on the envelope. Then there follow n lines with two integers each ΓÇö description of the stamps. Each stamp is described with indexes of the cities between which a letter is sent. The indexes of cities are integers from 1 to 10 9 . Indexes of all the cities are different. Every time the letter is sent from one city to another, exactly one stamp is put on the envelope. It is guaranteed that the given stamps correspond to some valid route from some city to some other city.

## Output

Output n ΓÇë+ΓÇë1 numbers ΓÇö indexes of cities in one of the two possible routes of the letter.

## Examples

Example 1:
```
2
1 100
100 2
```
```
2 100 1
```
