# E. Double-Rift Dial

**Submission:** https://codeforces.com/contest/2250/problem/E

**Limits:** 2 seconds / 256 megabytes

**Tags:** data structures, dfs and similar, dsu, implementation, two pointers

## Problem Statement

A permutation `p` of length `n` is written clockwise on a circular dial.

Choose a starting position `s` (`1 <= s <= n`) and read one full circle
clockwise from `p_s`, wrapping around after `p_n`. The resulting sequence is

```text
q = [p_s, p_{s+1}, ..., p_n, p_1, ..., p_{s-1}],
```

which also has a length of `n`.

For any non-empty prefix of this sequence `[q_1, q_2, ..., q_k]` (`k >= 1`),
let `S` be the corresponding set of values, that is,
`S = {q_1, q_2, ..., q_k}`. Split `S` into maximal segments of consecutive
integers, and we call these segments the blocks of `S`.

For example, `S = {1, 2, 5, 7, 8, 9}` has `3` blocks:
`{1, 2}`, `{5}`, and `{7, 8, 9}`.

A starting position `s` is called good if and only if, for every non-empty
prefix of `q`, the corresponding set `S` has at most `2` blocks.

Find the number of good starting positions.

A permutation of length `n` is an array consisting of `n` distinct integers
from `1` to `n` in arbitrary order. For example, `[2, 3, 1, 5, 4]` is a
permutation, but `[1, 2, 2]` is not a permutation (`2` appears twice), and
`[1, 3, 4]` is also not a permutation (`n = 3` but there is `4` in the array).

## Input

Each test contains multiple test cases. The first line contains the number of
test cases `t` (`1 <= t <= 10^4`). The description of the test cases follows.

The first line of each test case contains one integer `n`
(`1 <= n <= 2 * 10^5`), the length of `p`.

The second line of each test case contains `n` integers
`p_1, p_2, ..., p_n` (`1 <= p_i <= n`, all `p_i` are distinct), the elements
of `p`.

It is guaranteed that the sum of `n` over all test cases does not exceed
`2 * 10^5`.

## Output

For each test case, print one integer, the number of good starting positions.

## Example

### Input

```text
4
1
1
5
1 3 5 2 4
6
1 2 4 5 3 6
7
1 3 5 7 2 4 6
```

### Output

```text
1
4
3
0
```

## Note

In the first test case, there is only one starting position. Every non-empty
prefix contains the single value `1`, so it has one block. Thus, this position
is good.

In the second test case, after reading the first `3` numbers from position `1`,
the set is `{1, 3, 5}` and has `3` blocks. Thus, position `1` is not good. Each
of the other `4` positions is good.
