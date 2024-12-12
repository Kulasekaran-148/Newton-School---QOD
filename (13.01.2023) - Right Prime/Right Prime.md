# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Find the minimum prime number greater than or equal to X.

### Constraints

- $2 ≤ X ≤ 105$

## Input

The only line of the input contains a single integer X

### Example 1

**Input:**

```plain
20
```

**Output:**

```plain
23
```

### Example 2

**Input:**

```plain
99992
```

**Output:**

```plain
100003
```

### Example 3

**Input:**

```plain
2
```

**Output:**

```plain
2
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
#include <stdlib.h>
int main()
{
    int n, flag = 1, i;
    scanf("%d", &n);
    if (n == 2 || n == 3)
    {
        printf("%d", n);
    }
    else if (flag == 1)
    {
        for (i = 2; i <= n / 2; i++)
        {
            if (n % i == 0)
            {
                // printf("Hello");
                flag = 0;
                n++;
                break;
            }
            else if (i == n / 2)
            {
                // printf("Whats up");
                printf("%d", n);
            }
        }
    }
    if (flag == 0)
    {
        // printf("\nNice");
        for (i = 2; i <= n / 2; i++)
        {
            if (n % i == 0)
            {
                // printf("\nGood day[%d][%d]",i,n);
                n++;
                i = 1;
            }
            else if (i == ((n / 2)))
            {
                // printf("\nProgram[%d][%d]",i,n);
                printf("%d", n);
            }
        }
    }
    return 0;
}
```
