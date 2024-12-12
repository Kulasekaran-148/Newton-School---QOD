# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Newton has $2$ strings $P$ and $Q$. He wants to create a new string $Z$. String $Z$ can only be formed by concatenating $Q$ and $P$ in this order without any white spaces.

### Constraints

- 1 ≤ |P| ≤ 103
- 1 ≤ |Q| ≤ 103

## Input

The first line of the input contains two space separated strings P and Q

```plain
P Q
```

### Example 1

**Input:**

```plain
school newton
```

**Output:**

```plain
newtonschool
```

### Example 2

**Input:**

```plain
newton school
```

**Output:**

```plain
schoolnewton
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
#include <string.h>

int main() {
    char s1[1000], s2[1000];
    scanf("%s",&s1);
    scanf("%s",&s2);
    printf("%s%s",s2,s1);
}
```
