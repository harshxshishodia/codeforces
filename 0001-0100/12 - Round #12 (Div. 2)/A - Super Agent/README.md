# A. Super Agent

**Submission:** https://codeforces.com/contest/12/problem/A

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

There is a very secret base in Potatoland where potato mash is made according to a special recipe. The neighbours from Porridgia decided to seize this recipe and to sell it to Pilauland. For this mission they have been preparing special agent Pearlo for many years. When, finally, Pearlo learned all secrets of espionage, he penetrated into the Potatoland territory and reached the secret base.

Now he is standing at the entrance, but to get inside he need to pass combination lock. Minute ago one of the workers entered the password on the terminal and opened the door. The terminal is a square digital keyboard 3ΓÇë├ùΓÇë3 with digits from 1 to 9 .

Pearlo knows that the password consists from distinct digits and is probably symmetric with respect to the central button of the terminal. He has heat sensor which allowed him to detect the digits which the worker pressed. Now he wants to check whether the password entered by the worker is symmetric with respect to the central button of the terminal. This fact can Help Pearlo to reduce the number of different possible password combinations.

## Input

Input contains the matrix of three rows of three symbols each. Symbol ┬½ X ┬╗ means that the corresponding button was pressed, and ┬½ . ┬╗ means that is was not pressed. The matrix may contain no ┬½ X ┬╗, also it may contain no ┬½ . ┬╗.

## Output

Print YES if the password is symmetric with respect to the central button of the terminal and NO otherwise.

## Examples

Example 1:
```
XX.
...
.XX
```
```
YES
```

## Note

If you are not familiar with the term ┬½central symmetry┬╗, you may look into http://en.wikipedia.org/wiki/Central_symmetry
