# E. Parade

**Submission:** https://codeforces.com/contest/35/problem/E

**Limits:** 2 seconds / 64 megabytes

## Problem Statement

No Great Victory anniversary in Berland has ever passed without the war parade. This year is not an exception. ThatΓÇÖs why the preparations are on in full strength. Tanks are building a line, artillery mounts are ready to fire, soldiers are marching on the main square... And the air forces general Mr. Generalov is in trouble again. This year a lot of sky-scrapers have been built which makes it difficult for the airplanes to fly above the city. It was decided that the planes should fly strictly from south to north. Moreover, there must be no sky scraper on a planeΓÇÖs route, otherwise the anniversary will become a tragedy. The Ministry of Building gave the data on n sky scrapers (the rest of the buildings are rather small and will not be a problem to the planes). When looking at the city from south to north as a geometrical plane, the i -th building is a rectangle of height h i . Its westernmost point has the x-coordinate of l i and the easternmost ΓÇö of r i . The terrain of the area is plain so that all the buildings stand on one level. Your task as the Ministry of DefenceΓÇÖs head programmer is to find an enveloping polyline using the data on the sky-scrapers. The polylineΓÇÖs properties are as follows:

 
- If you look at the city from south to north as a plane, then any part of any building will be inside or on the boarder of the area that the polyline encloses together with the land surface. 
- The polyline starts and ends on the land level, i.e. at the height equal to 0. 
- The segments of the polyline are parallel to the coordinate axes, i.e. they can only be vertical or horizontal. 
- The polylineΓÇÖs vertices should have integer coordinates. 
- If you look at the city from south to north the polyline (together with the land surface) must enclose the minimum possible area. 
- The polyline must have the smallest length among all the polylines, enclosing the minimum possible area with the land. 
- The consecutive segments of the polyline must be perpendicular. 
 Picture to the second sample test (the enveloping polyline is marked on the right).

## Input

The first input line contains integer n ( 1ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë100000 ). Then follow n lines, each containing three integers h i , l i , r i ( 1ΓÇëΓëñΓÇë h i ΓÇëΓëñΓÇë10 9 ,ΓÇëΓÇë-ΓÇë10 9 ΓÇëΓëñΓÇë l i ΓÇë<ΓÇë r i ΓÇëΓëñΓÇë10 9 ).

## Output

In the first line output integer m ΓÇö amount of vertices of the enveloping polyline. The next m lines should contain 2 integers each ΓÇö the position and the height of the polylineΓÇÖs vertex. Output the coordinates of each vertex in the order of traversing the polyline from west to east. Remember that the first and the last vertices of the polyline should have the height of 0.

## Examples

Example 1:
```
2
3 0 2
4 1 3
```
```
6
0 0
0 3
1 3
1 4
3 4
3 0
```
