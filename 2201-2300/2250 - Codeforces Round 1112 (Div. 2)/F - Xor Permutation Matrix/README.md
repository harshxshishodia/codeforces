# F. Xor Permutation Matrix

**Submission:** https://codeforces.com/contest/2250/problem/F

**Limits:** 2 seconds / 512 megabytes

**Tags:** bitmasks, constructive algorithms, math

## Problem Statement

You are given two integers `n` and `x` (`0 <= x <= n - 1`).

Construct a matrix `A` of size `n * n` satisfying all of the following
conditions:

- For every `1 <= i, j <= n`, `0 <= A_{i,j} <= n - 1`.
- Every row in `A` forms a permutation of `0, 1, ..., n - 1`.
- Every column in `A` forms a permutation of `0, 1, ..., n - 1`.
- For every `1 <= i, j <= n - 1`,
  `A_{i,j} XOR A_{i+1,j} XOR A_{i,j+1} XOR A_{i+1,j+1} = x`.

Here, `XOR` denotes the bitwise XOR operation.

Or determine that no such matrix exists.

## Input

Each test contains multiple test cases. The first line contains the number of
test cases `t` (`1 <= t <= 180`). The description of the test cases follows.

The only line of each test case contains two integers `n` and `x`
(`2 <= n <= 2500`, `0 <= x < n`).

It is guaranteed that the sum of `n` over all test cases does not exceed
`2500`.

## Output

For each test case, output `-1` if no such matrix exists. Otherwise, output any
valid `n` lines of the matrix.

If several valid matrices exist, you may output any of them.

## Example

### Input

```text
5
2 0
2 1
3 0
4 1
4 0
```

### Output

```text
0 1
1 0
-1
-1
0 2 1 3
2 1 3 0
1 3 0 2
3 0 2 1
0 1 2 3
1 0 3 2
2 3 0 1
3 2 1 0
```

## Note

In the first test case, the displayed matrix has both rows and columns equal
to permutations of `0, 1`, and its only adjacent `2 * 2` submatrix has XOR
`0`.

The second and third test cases are impossible. In the last two test cases,
every adjacent `2 * 2` submatrix has XOR, respectively, `1` and `0`.
