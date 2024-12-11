# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Expected Output](#expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Python Solution](#python-solution)
- [C Solution](#c-solution)

## Problem Description

Rohit loves to play with balls. He removed $A$ balls from a box that contained $N$ balls and then put $B$ new balls into that box. How many balls does the box contain now?

### Constraints

- $100 \leq N \leq 200$
- $1 \leq A, B \leq 100$
- All values in the input are integers.

## Input

The input consists of three space-separated integers:

```plain
N A B
```

## Expected Output

Print the answer as an integer.

### Example 1

**Input:**

```plain
100 1 2
```

**Output:**

```plain
101
```

### Example 2

**Input:**

```plain
100 2 1
```

**Output:**

```plain
99
```

## Intuition

1. Subtract $A$ balls from the initial count $N$.
2. Add $B$ balls to the result.
3. Return the final count as the output.

## Complexity Analysis

### Time Complexity

- The calculation involves basic arithmetic operations, so the time complexity is $O(1)$.

### Space Complexity

- No additional data structures are used, so the space complexity is $O(1)$.

## Python Solution

Below is the Python code for solving the problem:

```python
n, a, b = map(int, input().split())
print(n - a + b)
```

## C Solution

Below is the C code for solving the problem:

```c
#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int n, a, b;
    scanf("%d %d %d", &n, &a, &b);
    printf("%d", n - a + b);
    return 0;
}
```
