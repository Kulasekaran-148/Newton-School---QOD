# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

For an integer $n$, let $S(n)$ be the sum of digits in the decimal notation of $n$. For example, we have
$S(123)=1+2+3=6$. Given two $3$- digit integers $A\ and\ B$, find the greater of $S(A)$ and $S(B)$.

### Constraints

- All values in the input are integers.
- $100 \leq A,\ B \leq 999$

## Input

The input consists of two space-separated integers A and B.

```plain
A B
```

### Example 1

**Input:**

```plain
123 234
```

**Output:**

```plain
9
```

### Example 2

**Input:**

```plain
593 953
```

**Output:**

```plain
17
```

### Example 3

**Input:**

```plain
100 999
```

**Output:**

```plain
27
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
sum1=0
sum2=0
while(a>0):
    sum1+=a%10
    a/=10
    sum2+=b%10
    b/=10
    sum1=int(sum1)
    sum2=int(sum2)
print(max(sum1,sum2),end="")
```
