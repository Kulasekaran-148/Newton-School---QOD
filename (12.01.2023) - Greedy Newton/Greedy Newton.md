# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Newton has $A$ cookies, and Einstein has $B$ cookies. Newton will do the following action $K$ times:

1) If Newton has one or more cookies, eat one of his cookies.
2) Otherwise, if Einstein has one or more cookies, eat one of Einstein's cookies.
3) If they both have no cookies, do nothing.

In the end, how many cookies will Newton and Einstein have, respectively?

### Constraints

- $0 ≤ A ≤ 1012$
- $0 ≤ B ≤ 1012$
- $0 ≤ K ≤ 1012$

## Input

The first line of the input contains 3 integers, $A,\ B\ and\ K$

```plain
A B K
```

### Example 1

**Input:**

```plain
2 3 3
```

**Output:**

```plain
0 2
```

### Example 2

**Input:**

```plain
500000000000 500000000000 1000000000000
```

**Output:**

```plain
0 0
```

## Intuition

- abcd

## Complexity Analysis

### Time Complexity

- O(N)

### Space Complexity

- O(N)

## Solution

```c
#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    long long ncookies, ecookies, count, i;
    scanf("%lld%lld%lld",&ncookies, &ecookies, &count);
    if(count<ncookies)
    {
        ncookies=ncookies-count;
    }
    else
    {
        count=count-ncookies;
        ncookies=0;
        if(count<ecookies){
            ecookies=ecookies-count;
        }
        else{
            ecookies=0;
        }
        
    }
    printf("%lld %lld",ncookies,ecookies);
    return 0;
}
```
