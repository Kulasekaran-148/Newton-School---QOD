# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Is it possible to get a sum of B when throwing a die with six faces 1, 2, …, 6 A times? If it is possible to get a sum of B, print Yes; otherwise, print No.


### Constraints

- $1 \leq A \leq 100$
- $1 \leq B \leq 1000$
- A and B are integers

## Input

The input consists of two space-separated integers.

```plain
A B
```

### Example 1

**Input:**

```plain
2 11
```

**Output:**

```plain
Yes
```

### Example 2

**Input:**

```plain
2 13
```

**Output:**

```plain
No
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
#include <stdio.h>
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    if(b<=(a*6) && b>=a)
        {printf("Yes");}
    else{printf("No");}
    return 0;
}
```
