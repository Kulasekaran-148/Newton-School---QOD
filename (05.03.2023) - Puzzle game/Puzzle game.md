# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Bob challenged Alexa with a puzzle. He asked her to count how many integers not less than
A and not more than B are there? Help Alexa to win. Print the number of integers not less than A and not more than B.

### Constraints

- $1 \leq A \leq 100$
- $1 \leq B \leq 100$
- A and B are integers

## Input

The input consists of two space separated integers.

```plain
A B
```

### Example 1

**Input:**

```plain
2 4
```

**Output:**

```plain
3
```

### Example 2

**Input:**

```plain
10 100
```

**Output:**

```plain
91
```

### Example 3

**Input:**

```plain
3 2
```

**Output:**

```plain
0
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
a,b = map(int,input().split())
if(a<b):
    print(b-a+1, end="")
else:
    print(0, end="")
```
