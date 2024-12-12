# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Newton is standing before a typical staircase with $N$ steps. Newton is standing on the $0_{th}$ step and wants to go to the $N_{th}$ step. To reach the top he can either take a single step or he can take a double step (two steps) at the same time.

However, $M$ of the $N$ steps are broken i.e. $S_1, S_2, ... , S_M$ are broken and Newton cannot visit those steps,

Find out the number of different ways in which Newton can climb to the top of the staircase. Since the number can be very large, find it modulo $1,000,000,007$

### Constraints

- $1 ≤ N ≤ 2 x 105$
- $0 ≤ M ≤ N - 1$
- $1 ≤ S_1 < S_2, < ... < S_M ≤ N - 1$

## Input

The first line contains two integers, $N$ and $M$.
The next $M$ lines contains a single integer each, $S_i$

### Example 1

**Input:**

```plain
6 1
3
```

**Output:**

There are four ways to climb up the stairs, as follows:

- 0→1→2→4→5→6
- 0→1→2→4→6
- 0→2→4→5→6
- 0→2→4→6

```plain
4
```

### Example 2

**Input:**

```plain
100 5
1
23
45
67
89
```

**Output:**

```plain
608200469
```

## Intuition

- abcd

## Complexity Analysis

### Time Complexity

- O(N)

### Space Complexity

- O(N)

## Solution

```C
#include <stdio.h>
#include <stdbool.h>

#define MOD 1000000007

int num_ways(int n, int m, int broken_steps[m])
{
    bool is_broken[n + 1];
    for (int i = 0; i <= n; i++)
    {
        is_broken[i] = false;
    }
    for (int i = 0; i < m; i++)
    {
        is_broken[broken_steps[i]] = true;
    }

    int dp[n + 1];
    dp[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        dp[i] = 0;
        if (!is_broken[i])
        {
            dp[i] = dp[i - 1];
        }
        if (!is_broken[i] && i > 1 && !is_broken[i - 2])
        {
            dp[i] = (dp[i] + dp[i - 2]) % MOD;
        }
    }
    return dp[n];
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    int broken_steps[m];
    for (int i = 0; i < m; i++)
    {
        scanf("%d", &broken_steps[i]);
    }
    printf("%d", num_ways(n, m, broken_steps));
    return 0;
}
```
