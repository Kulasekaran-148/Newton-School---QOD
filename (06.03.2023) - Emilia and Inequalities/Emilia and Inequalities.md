# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Emilia loves to play with numbers. She is given integers $A, B,$ and $C$. Determine whether $A_2 + B_2 < C_2$ holds true.

### Constraints

- $0 \leq A \leq 1000$
- $0 \leq B \leq 1000$
- $0 \leq C \leq 1000$
- $A, B,$ and $C$ are integers.

## Input

The input consists of three space-separated integers $A, B,$ and $C$.

### Example 1

**Input:**

```plain
2 2 4
```

**Output:**

```plain
Yes
```

### Example 2

**Input:**

```plain
10 10 10
```

**Output:**

```plain
No
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
a,b,c=map(int,input().split())
if(a**2+b**2<c**2):
    print("Yes",end="")
else:
    print("No",end="")
```
