# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Newton has $N$ different weights indexed from $1$ to $N$ i.e. $W_1$, $W_2$, ... , $W_N$.

Newton is having a hard time trying to balance the weights. He wants to divides the weights into 2 parts.

To do so, he is choosing an integer $X$ and merging all the weights having index not more than $X$ into a single weight $S_1$ and the remaining weights into a single weight $S_2$.

He needs to choose the index X in such a way that the absolute difference of the weights $S_1$ and $S_2$ is the minimum.

Find the least possible absolute difference that Newton can come up with.

### Constraints

- $2 \leq N \leq 1000$
- $1 \leq W_i \leq 1000$

## Input

The first line of the input contains a single integer N.

The next line of the input contains N space separated integers $W_1$, $W_2$, ... , $W_N$

### Example 1

**Input:**

```plain
4
1 2 3 6
```

**Output:**

```plain
0
```

### Example 2

**Input:**

```plain
4
1 3 1 1
```

**Output:**

```plain
2
```

### Example 3

**Input:**

```plain
8
27 23 76 2 3 5 62 52
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
int main() {
    int count,weights[100],i,j=0,bal1=0,bal2=0,temp=100;
    scanf("%d",&count);
    for(i=0;i<count;i++)
    {
        scanf("%d",&weights[i]);
    }
    for(i=0;i<count;i++)
    {
        for(j=0;j<count;j++)
        {
            if(i>=j)
            {
                bal1=bal1+weights[j];
                // printf("\nIteration[%d]Bal1=%d",i,bal1);
            }
            else
            {
                bal2=bal2+weights[j];
                // printf("\nIteration[%d]Bal2=%d",i,bal2);
            }
        }
        if(bal1>bal2)
        {
            if((bal1-bal2)<temp){
                temp=(bal1-bal2);
            }
        }
        else
        {
            if((bal2-bal1)<temp){
                temp=(bal2-bal1);
            }
        }
        bal1=0;
        bal2=0;
    }
    printf("%d",temp);
}
```
