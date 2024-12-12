# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

We have $A$ cards, each of which has an integer $1$ written on it. Similarly, we also have $B$ cards with $0s$ and $C$ cards with $−1s$.
We will pick up K among these cards. What is the maximum possible sum of the numbers written on the cards chosen?

### Constraints

- All values in input are integers.
- $ 0 ≤ A, B, C$
- $1 ≤ K ≤ A+B+C ≤ 2×10^9$

## Input

The input consists of 4 space separated integers as follows :

```plain
A B C K
```

### Example 1

**Input:**

```plain
2 1 1 3
```

**Output:**

```plain
2
```

### Example 2

**Input:**

```plain
1 2 3 4
```

**Output:**

```plain
0
```

### Example 3

**Input:**

```plain
4
8 9 10 11
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
a,b,c,k = map(int,input().split())
result=0;
if(k>=a):
    result+=a
    k-=a
else:
    result+=k*1
    k=0
if(k>=b):
    k-=b
elif(k>0):
    result-=k*b
    k=0
if(k>=c):
    result-=c
    k-=c
    k=0
elif(k>0):
    result-=k*(1)
print(result,end="")
```
