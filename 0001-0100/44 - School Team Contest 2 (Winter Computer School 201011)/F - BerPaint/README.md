# F. BerPaint

**Submission:** https://codeforces.com/contest/44/problem/F

**Limits:** 5 seconds / 256 megabytes

## Problem Statement

Anfisa the monkey got disappointed in word processors as they aren't good enough at reflecting all the range of her emotions, that's why she decided to switch to graphics editors. Having opened the BerPaint, she saw a white rectangle W ΓÇë├ùΓÇë H in size which can be painted on. First Anfisa learnt to navigate the drawing tool which is used to paint segments and quickly painted on that rectangle a certain number of black-colored segments. The resulting picture didn't seem bright enough to Anfisa, that's why she turned her attention to the "fill" tool which is used to find a point on the rectangle to paint and choose a color, after which all the area which is the same color as the point it contains, is completely painted the chosen color. Having applied the fill several times, Anfisa expressed her emotions completely and stopped painting. Your task is by the information on the painted segments and applied fills to find out for every color the total area of the areas painted this color after all the fills.

## Input

The first input line has two integers W and H ( 3ΓÇëΓëñΓÇë W ,ΓÇë H ΓÇëΓëñΓÇë10 4 ) ΓÇö the sizes of the initially white rectangular painting area. The second line contains integer n ΓÇö the number of black segments ( 0ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100 ). On the next n lines are described the segments themselves, each of which is given by coordinates of their endpoints x 1 ,ΓÇë y 1 ,ΓÇë x 2 ,ΓÇë y 2 ( 0ΓÇë<ΓÇë x 1 ,ΓÇë x 2 ΓÇë<ΓÇë W ,ΓÇë0ΓÇë<ΓÇë y 1 ,ΓÇë y 2 ΓÇë<ΓÇë H ). All segments have non-zero length. The next line contains preset number of fills m ( 0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë100 ). Each of the following m lines defines the fill operation in the form of " x y color ", where ( x ,ΓÇë y ) are the coordinates of the chosen point ( 0ΓÇë<ΓÇë x ΓÇë<ΓÇë W ,ΓÇë0ΓÇë<ΓÇë y ΓÇë<ΓÇë H ), and color ΓÇö a line of lowercase Latin letters from 1 to 15 symbols in length, determining the color. All coordinates given in the input are integers. Initially the rectangle is "white" in color, whereas the segments are drawn "black" in color.

## Output

For every color present in the final picture print on the single line the name of the color and the total area of areas painted that color with an accuracy of 10 ΓÇë-ΓÇë6 . Print the colors in any order.

## Examples

Example 1:
```
4 5
6
1 1 1 3
1 3 3 3
3 3 3 1
3 1 1 1
1 3 3 1
1 1 3 3
2
2 1 red
2 2 blue
```
```
blue 0.00000000
white 20.00000000
```

## Note

Initially the black segments painted by Anfisa can also be painted a color if any of the chosen points lays on the segment. The segments have areas equal to 0. That is why if in the final picture only parts of segments is painted some color, then the area, painted the color is equal to 0.
