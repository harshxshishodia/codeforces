# D. Permutation Cuts

**Submission:** https://codeforces.com/contest/2250/problem/D

**Limits:** 4 seconds / 256 megabytes

**Tags:** combinatorics, implementation, math

## Problem Statement

You are given an integer `n` and an array `a` of length `n - 1`.

For a permutation `p` of length `n`, define

```text
v_i = min(max(p_1, p_2, ..., p_i), max(p_{i+1}, p_{i+2}, ..., p_n)),
```

where `1 <= i <= n - 1`.

In other words, cut the permutation between positions `i` and `i + 1`, take
the maximum element on each side, and let `v_i` be the smaller of these two
values.

Your task is to count the number of permutations `p` of length `n` such that
`v_i = a_i` for each `1 <= i <= n - 1`.

Output the answer modulo `998244353`.

A permutation of length `n` is an array consisting of `n` distinct integers
from `1` to `n` in arbitrary order. For example, `[2, 3, 1, 5, 4]` is a
permutation, but `[1, 2, 2]` is not a permutation (`2` appears twice), and
`[1, 3, 4]` is also not a permutation (`n = 3` but there is `4` in the array).

## Input

Each test contains multiple test cases. The first line contains the number of
test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains one integer `n`
(`2 <= n <= 10^6`), the length of `p`.

The second line contains `n - 1` integers `a_1, a_2, ..., a_{n-1}`
(`1 <= a_i <= n`), the elements of `a`.

It is guaranteed that the sum of `n` over all test cases does not exceed
`10^6`.

## Output

For each test case, output one integer, the number of suitable permutations
modulo `998244353`.

## Example

### Input

```text
11
2
1
3
2 2
3
1 1
4
2 3 2
5
3 3 4 2
2
2
3
1 2
4
3 3 3
5
4 4 4 4
4
2 1 2
6
3 3 5 5 5
```

### Output

```text
2
2
0
0
2
0
2
4
12
0
8
```

## Note

In the first test case, both permutations `[1, 2]` and `[2, 1]` satisfy
`v_1 = 1`.

In the second test case, the only suitable permutations are `[2, 1, 3]` and
`[3, 1, 2]`.

In the third test case, no suitable permutation exists.
