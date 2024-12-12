# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Given is a positive integer $N$, where none of the digits is $0$. Let $k$ be the number of digits in $N$. We want to make a multiple of $3$ by erasing at least $0$ and at most $k−1$ digits from $N$ and concatenating the remaining digits without changing the order. Determine whether it is possible to make a multiple of $3$ in this way. If it is possible, find the minimum number of digits that must be erased to make such a number. If it is impossible to make a multiple of 3, print -1; otherwise, print the minimum number of digits that must be erased to make such a number.

### Constraints

- $1 \leq N \leq 10^{18}$
- None of the digits in N is 0.

## Input

The input consists of a single integer $N$.

### Example 1

**Input:**

```plain
35
```

**Output:**

```plain
1
```

### Example 2

**Input:**

```plain
369
```

**Output:**

```plain
0
```

### Example 3

**Input:**

```plain
6227384
```

**Output:**

```plain
1
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
n=input()
result=0
k=0
if(True):
    for i in range(len(n)):
        result+=int(n[i])
    if(result%3==0):
        print('0',end="")
        exit()
for i in range(len(n)):
    dig=result%3
    if str(dig) in n:
        result-=dig
        k+=1
    else:
        revstring=n[::-1]
        result=result-int(revstring[i]) 
        k+=1
    if(result%3==0 and result!=0):
        print(k,end="")
        exit()
print("-1",end="")
```
