# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

There are $4$ squares lined up horizontally. You are given a string $S$ of length $4$ consisting of $0$ and $1$.
If the $i_{th}$ character of $S$ is $1$, there is a person in the $i_{th}$ square from the left; if the $i_{th}$ character of
$S$ is $0$, there is no person in the $i_{th}$ square from the left.
Now, everyone will move to the next square to the right simultaneously. With this move, the person who was originally in the rightmost square will disappear. Determine if there will be a person in each square after the move. Print the result as a string in the same format as $S$.

### Constraints

- $S$ is a string of length $4$ consisting of $0$ and $1$.

## Input

The input consists of a single string.

### Example 1

**Input:**

```plain
1011
```

**Output:**

```plain
0101
```

### Example 2

**Input:**

```plain
0000
```

**Output:**

```plain
0000
```

### Example 3

**Input:**

```plain
1111
```

**Output:**

```plain
0111
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
a = input()
b = [0,a[0],a[1],a[2]]
for i in range(4):
    print(str(b[i]),end="")
```
