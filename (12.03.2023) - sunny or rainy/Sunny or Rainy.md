# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

You are given a string $S$, which represents a weather forecast for the seven days starting tomorrow. The $i_{th}$ of those seven days is forecast to be sunny if the ith character of $S$ is $o$, and rainy if that character is $x$. Tell us whether the Nth day is forecast to be sunny.


### Constraints

- $N$ is an integer between $1$ and $7$ (inclusive).
- $S$ is a string of length $7$ consisting of $o$ and $x$.

## Input

The first line of the input consists of an integer $N$.
The second line of the input consists of a string.

### Example 1

**Input:**

```plain
4
oooxoox
```

**Output:**

```plain
No
```

### Example 2

**Input:**

```plain
7
ooooooo
```

**Output:**

```plain
Yes
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
n = int(input())
s = input()
if(s[n-1]=='o'):
    print('Yes',end="")
else:
    print('No',end="")
```
