# C. System Administrator

**Submission:** https://codeforces.com/contest/22/problem/C

**Limits:** 1 second / 256 megabytes

## Problem Statement

Bob got a job as a system administrator in X corporation. His first task was to connect n servers with the help of m two-way direct connection so that it becomes possible to transmit data from one server to any other server via these connections. Each direct connection has to link two different servers, each pair of servers should have at most one direct connection. Y corporation, a business rival of X corporation, made Bob an offer that he couldn't refuse: Bob was asked to connect the servers in such a way, that when server with index v fails, the transmission of data between some other two servers becomes impossible, i.e. the system stops being connected. Help Bob connect the servers.

## Input

The first input line contains 3 space-separated integer numbers n , m , v ( 3ΓÇëΓëñΓÇë n ΓÇëΓëñΓÇë10 5 ,ΓÇë0ΓÇëΓëñΓÇë m ΓÇëΓëñΓÇë10 5 ,ΓÇë1ΓÇëΓëñΓÇë v ΓÇëΓëñΓÇë n ), n ΓÇö amount of servers, m ΓÇö amount of direct connections, v ΓÇö index of the server that fails and leads to the failure of the whole system.

## Output

If it is impossible to connect the servers in the required way, output -1 . Otherwise output m lines with 2 numbers each ΓÇö description of all the direct connections in the system. Each direct connection is described by two numbers ΓÇö indexes of two servers, linked by this direct connection. The servers are numbered from 1. If the answer is not unique, output any.

## Examples

Example 1:
```
5 6 3
```
```
1 2
2 3
3 4
4 5
1 3
3 5
```
