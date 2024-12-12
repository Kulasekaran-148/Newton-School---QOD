# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Edward is playing the slots. The result of a spin is represented by three uppercase English letters $C_1, C_2, and C_3$. It is considered a win when all of them are the same letter.
Determine whether Edward will win or not. If the result is a win, print Won; otherwise, print Lost.

### Constraints

- $1 \leq A \leq 100$
- $1 \leq B \leq 1000$
- $S$ consists of 3 characters all of which are uppercase English letters.


## Input

The input consists of a string $S$

### Example 1

**Input:**

```plain
"SSS"
```

**Output:**

```plain
"Won"
```

### Example 2

**Input:**

```plain
"WVW"
```

**Output:**

```plain
"Lost"
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
s1 = input()
if(s1[0]==s1[1] and s1[0]==s1[2]):
    print("Won",end="")
else:
    print("Lost",end="")
```
