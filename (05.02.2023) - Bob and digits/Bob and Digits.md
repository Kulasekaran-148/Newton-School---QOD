# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Bob loves to play with numbers. He has an integer N. Print the number of digits that N has in base K.

### Constraints

- $1 \leq N \leq 109$
- $2 \leq K \leq 10$
- N and K are integers

## Input

The input contains two space-separated integers in the following format:

```plain
N K
```

### Example 1

**Input:**

```plain
11 2
```

**Output:**

```plain
4
```

### Example 2

**Input:**

```plain
1010101 10
```

**Output:**

```plain
7
```

### Example 3

**Input:**

```plain
314159265 3
```

**Output:**

```plain
18
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
n,k=map(int,input().split())
def dec_to_base(num,base): 
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10) 
        num //= base
    base_num = base_num[::-1] 
    return base_num
converted_num = str(dec_to_base(n,k))
print(len(converted_num),end="")
```
