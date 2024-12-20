# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

There are $3$ points, $X,\ Y\ and\ Z$ on a road.

- It takes $A$ hours to travel from X to Y or from $Y\ to\ X$.
- It takes $B$ hours to travel from Y to Z or from $Z\ to\ Y$.
- It takes $C$ hours to travel from X to Z or from $Z\ to\ X$.

- Newton is given the time required to travel between the points, i.e. $A,\ B\ and\ C$. He wants you to help him to calculate the minimum time needed to visit all the points once, starting from any point of your choice.

### Constraints

- $1 \leq A,\ B,\ C \leq 1000$

## Input

The first and the only line of the input contains $3$ integers, $A,\ B\ and\ C$.

### Example 1

**Input:**

```plain
1 3 4
```

**Output:**

The minimum distance to travel all 3 points can be found is we start at A and then go to B and then to C.

$A\ ->\ B\ ->\ C = 1 + 3 = 4$

```plain
4
```

### Example 2

**Input:**

```plain
3 2 3
```

**Output:**

```plain
5
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
#include <string.h>
int main()
{
    int a, b, c, result;
    scanf("%d%d%d", &a, &b, &c);
    if (a < b && a < c)
    {
        result = result + a;
        if (b < c)
        {
            result = result + b;
        }
        else
        {
            result = result + c;
        }
    }
    else if (b < a && b < c)
    {
        result = result + b;
        if (a < c)
        {
            result = result + a;
        }
        else
        {
            result = result + c;
        }
    }
    else
    {
        result = result + c;
        if (a < b)
        {
            result = result + a;
        }
        else
        {
            result = result + b;
        }
    }
    printf("%d", result);
}
```
