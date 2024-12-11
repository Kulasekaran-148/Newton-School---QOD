# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Expected Output](#expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Emilia loves to play with integers. Print how many distinct integers there are in given five integers A, B, C, D, and E.

### Constraints

- $0 \leq A, B, C, D, E \leq 100$
- All values in the input are integers

## Input

The input consists of 5 space-separated integers.

```plain
A B C D E
```

## Expected Output

### Example 1

**Input:**

```plain
31 9 24 31 24
```

**Output:**

```plain
3
```

### Example 2

**Input:**

```plain
0 0 0 0 0
```

**Output:**

```plain
1
```

## Intuition

- Use a hashmap to map the inputs
- Maintain a count of the values being pushed into the hashmap
- return the count

## Complexity Analysis

### Time Complexity

- O(N)

### Space Complexity

- O(N)

## Solution

```python
a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
print(len(b),end="")
```
