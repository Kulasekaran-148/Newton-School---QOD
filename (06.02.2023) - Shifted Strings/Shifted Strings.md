# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

We have a string S consisting of uppercase English letters. Additionally, an integer N will be given. Shift each character of S by N in alphabetical order (see below), and print the resulting string. We assume that A follows Z. For example, shifting A by 2 results in C (A → B → C), and shifting Y by 3 results in B (Y → Z → A → B).



### Constraints

- $1 \leq A \leq 100$
- $1 \leq B \leq 1000$
- A and B are integers

## Input

The input contains a number and a string separated by a new line.

```plain
N
S
```

### Example 1

**Input:**

```plain
2
ABCXYZ
```

**Output:**

```plain
CDEZAB
```

### Example 2

**Input:**

```plain
0
ABCXYZ
```

**Output:**

```plain
ABCXYZ
```

### Example 3

**Input:**

```plain
13
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

**Output:**

```plain
NOPQRSTUVWXYZABCDEFGHIJKLM
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
n=int(input())
n=n%26
s=input()

def shift_alphabet(s, n):
    result = ""
    n = n % 26
    for char in s:
        if char.isalpha() and char.isupper():
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            result += char
    return result
print(shift_alphabet(s,n))
```
