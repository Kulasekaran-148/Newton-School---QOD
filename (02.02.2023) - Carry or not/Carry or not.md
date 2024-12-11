# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Expected Output](#expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Available Solutions](#available-solutions)
- [Solution](#solution)

# Available Solutions
- [Python](#solution)
## Problem Description

You are given positive integers $A$ and $B$.

Let us calculate $A + B$ (in decimal). If it does not involve a carry, print `Easy`; if it does, print `Hard`.

### Constraints

- $1 \leq A, B \leq 10^{18}$
- $A$ and $B$ are integers.

## Input

The input contains two space-separated numbers:

```plain
A B
```

## Expected Output

If the calculation does not involve a carry, print `Easy`; otherwise, print `Hard`.

### Example 1

**Input:**

```plain
229 390
```

**Output:**

```plain
Hard
```

### Example 2

**Input:**

```plain
123456789 9876543210
```

**Output:**

```plain
Easy
```

## Intuition

1. Compare digits of $A$ and $B$ from the least significant digit (rightmost) to the most significant digit (leftmost).
2. If at any position the sum of corresponding digits exceeds 9, there is a carry, and the output is `Hard`.
3. If no such position exists, the output is `Easy`.

## Complexity Analysis

### Time Complexity

- Adding and comparing digits for the smaller of the two numbers' lengths is $O(n)$, where $n$ is the maximum number of digits in $A$ or $B$.
- Overall complexity is $O(n)$.

### Space Complexity

- Space is used for storing the reversed and padded strings of $A$ and $B$, which is $O(n)$.

## Solution

Below is the Python code for solving the problem:

```python
a, b = map(str, input().split())
flag = 0

# Pad the shorter number with leading zeros
while len(a) > len(b):
    b = "0" + b
while len(b) > len(a):
    a = "0" + a

# Reverse strings for digit-by-digit comparison
a = a[::-1]
b = b[::-1]

# Check for carry in digit addition
for i in range(len(a)):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard", end="")
        flag = 1
        break

if flag == 0:
    print("Easy", end="")
```
