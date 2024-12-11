# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Expected Output](#expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Python Solution](#python-solution)

## Problem Description

There is a container with $A$ cyan balls. Alexa will do the following operation as many times as they like (possibly zero times):

Add $B$ cyan balls and $C$ red balls into the container.

Alexa's objective is to reach a situation where the number of cyan balls in the container is at most $D$ times the number of red balls in it.

Determine whether the objective is achievable. If it is achievable, find the minimum number of operations needed to achieve it.

### Constraints

- $1 \leq A, B, C, D \leq 10^5$
- All values in the input are integers.

## Input

The input contains four space-separated integers:

```plain
A B C D
```

## Expected Output

If Alexa's objective is achievable, print the minimum number of operations needed to achieve it. Otherwise, print -1.

### Example 1

**Input:**

```plain
5 2 3 2
```

**Output:**

```plain
2
```

### Example 2

**Input:**

```plain
6 9 2 3
```

**Output:**

```plain
-1
```

## Intuition

1. Check if the ratio condition can ever be satisfied by verifying if the increase in cyan balls ($B$) does not outweigh the increase in red balls ($C \times D$). If not, return -1.
2. Simulate the process:
   - Increment the number of cyan and red balls based on $B$ and $C$.
   - Count the number of iterations until the condition $\text{Cyan} \leq \text{Red} \times D$ is satisfied.
3. Return the number of iterations if the condition is met.

## Complexity Analysis

### Time Complexity

- **Worst Case:** $O(A / C)$ iterations if the condition is always achievable.
- **Best Case:** $O(1)$ if the condition is immediately met or determined to be impossible.

### Space Complexity

- $O(1)$: No additional data structures are required.

## Python Solution

Below is the Python code for solving the problem:

```python
a, b, c, d = map(int, input().split())
r = 0
operations = 0

if c * d <= b:
    print("-1", end="")
else:
    while a > r * d:
        a += b
        r += c
        operations += 1
    print(operations, end="")
```
