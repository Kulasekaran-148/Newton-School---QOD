# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Output](#expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Alexa will turn on the air conditioner if, and only if, the temperature of the room is 30 degrees Celsius or above. The current temperature of the room is \( X \) degrees Celsius. Will she turn on the air conditioner?

### Constraints

- $-40 \leq X \leq 40$
- $X$ is an integer.

## Input

The input consists of a single integer **X**.

## Expected Output

Print `Yes` if the air conditioner will turn on; otherwise, print `No`.

### Example 1

**Input:**

```plain
25
```

**Output:**

```plain
No
```

### Example 2

**Input:**

```plain
30
```

**Output:**

```plain
Yes
```

## Intuition

1. Check if the given temperature $X$ is 30 or higher.
2. If true, the air conditioner will turn on (`Yes`); otherwise, it will remain off (`No`).

## Complexity Analysis

### Time Complexity

- The condition check $X \geq 30$ is $O(1)$.
- Overall, the complexity is $O(1)$.

### Space Complexity

- No additional space is used apart from input storage, so the space complexity is $O(1)$.

## Solution

Below is the C code for solving the problem:

```c
#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int x;
    scanf("%d", &x);
    if (x >= 30) {
        printf("Yes");
    } else {
        printf("No");
    }
    return 0;
}
```
