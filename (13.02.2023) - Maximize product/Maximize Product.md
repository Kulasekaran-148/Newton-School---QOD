# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Given are integers $a,\ b,\ c,\ and\ d$. If $x$ and $y$ are integers and $a\ ≤\ x\ ≤\ b$ and $c\ ≤\ y\ ≤\ d$ hold, what is the maximum possible value of $x*y$ ?

## Input

The input consists of four space-separated integers.

```plain
a b c d
```

### Example 1

**Input:**

```plain
1 2 1 1
```

**Output:**

```plain
2
```

### Example 2

**Input:**

```plain
3 5 -4 -2
```

**Output:**

```plain
-6
```

### Example 3

**Input:**

```plain
-1000000000 0 -1000000000 0
```

**Output:**

```plain
1000000000000000000
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
a,b,c,d = map(int, input().split())
result=max(a*c,a*d,b*c,b*d)
print(result,end="")
```
