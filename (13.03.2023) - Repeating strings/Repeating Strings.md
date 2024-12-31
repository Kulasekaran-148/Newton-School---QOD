# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

You are given a string S consisting of lowercase English characters. The length of S is between 1 and 3, inclusive. Print the string of length 6 that is a repetition of S. It can be shown that there uniquely exists such a string under the Constraints of this problem.

### Constraints

- S is a string consisting of lowercase English characters of length between 1 and 3, inclusive.

## Input

The input consists of a string S

### Example 1

**Input:**

```plain
abc
```

**Output:**

```plain
abcabc
```

### Example 2

**Input:**

```plain
zz
```

**Output:**

```plain
zzzzzz
```

### Example 3

**Input:**

```plain
4
8 9 10 11
```

**Output:**

```plain
1
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
s = input()
length = len(s)
for i in range (int(6/length)):
    print(s,end="")
```
