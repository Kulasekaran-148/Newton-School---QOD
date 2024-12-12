# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

You are given an integer $N$. Do the following operation $K$ times on it and print the resulting integer. If $N$ is a multiple of $200$, divide it by $200$. Otherwise, see $N$ as a string and append $200$ to the end of it.

### Constraints

- All values in input are integers.
- $1 ≤ N ≤ 10^5$
- $1 ≤ K ≤ 20$

## Input

The input consists of two space separated integers as follows:

```plain
N K
```

### Example 1

**Input:**

```plain
2021 4
```

**Output:**

```plain
50531
```

### Example 2

**Input:**

```plain
40000 2
```

**Output:**

```plain
1
```

### Example 3

**Input:**

```plain
8691 20
```

**Output:**

```plain
84875488281
```

## Intuition

- abcd

## Complexity Analysis

### Time Complexity

- O(N)

### Space Complexity

- O(N)

## Solution

```python
n,k = map(int, input().split())
for i in range(k):
    if n%200==0:
        n/=200
        n=int(n)
        # print(i,n)
    else:
        n=str(n)
        n+="200"
        n=int(n)
        # print(i,n)
print(n,end="")
```
