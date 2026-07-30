# E. Multithreading

**Submission:** https://codeforces.com/contest/26/problem/E

**Limits:** 2 seconds / 256 megabytes

## Problem Statement

You are given the following concurrent program. There are N processes and the i -th process has the following pseudocode: 
 repeat n i times
 y i := y 
 y := y i ΓÇë+ΓÇë1 
end repeat
 
Here y is a shared variable. Everything else is local for the process. All actions on a given row are atomic, i.e. when the process starts executing a row it is never interrupted. Beyond that all interleavings are possible, i.e. every process that has yet work to do can be granted the rights to execute its next row. In the beginning y ΓÇë=ΓÇë0 . You will be given an integer W and n i , for i ΓÇë=ΓÇë1,ΓÇë... ,ΓÇë N . Determine if it is possible that after all processes terminate, y ΓÇë=ΓÇë W , and if it is possible output an arbitrary schedule that will produce this final value.

## Input

In the first line of the input you will be given two space separated integers N ( 1ΓÇëΓëñΓÇë N ΓÇëΓëñΓÇë100 ) and W ( ΓÇë-ΓÇë10 9 ΓÇëΓëñΓÇë W ΓÇëΓëñΓÇë10 9 ). In the second line there are N space separated integers n i ( 1ΓÇëΓëñΓÇë n i ΓÇëΓëñΓÇë1000 ).

## Output

On the first line of the output write Yes if it is possible that at the end y ΓÇë=ΓÇë W , or No otherwise. If the answer is No then there is no second line, but if the answer is Yes , then on the second line output a space separated list of integers representing some schedule that leads to the desired result. For more information see note.

## Examples

Example 1:
```
1 10
11
```
```
No
```

## Note

For simplicity, assume that there is no repeat statement in the code of the processes, but the code from the loop is written the correct amount of times. The processes are numbered starting from 1. The list of integers represent which process works on its next instruction at a given step. For example, consider the schedule 1 2 2 1 3 . First process 1 executes its first instruction, then process 2 executes its first two instructions, after that process 1 executes its second instruction, and finally process 3 executes its first instruction. The list must consists of exactly 2┬╖╬ú i ΓÇë=ΓÇë1... N ΓÇë n i numbers.
