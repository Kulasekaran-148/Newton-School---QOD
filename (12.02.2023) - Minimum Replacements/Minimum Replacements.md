# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

Given are two strings $S$ and $T$.
Let us change some of the characters in $S$ so that $T$ will be a substring of $S$. At least how many characters do we need to change?

### Constraints

- $1 <= |S|, |T| <= 1000$
- $S$ and $T$ consist of lowercase English letters.

## Input

The input consists of two strings separated by a line.

```plain
S
T
```

### Example 1

**Input:**

```plain
cabacc
abc
```

**Output:**

```plain
1
```

### Example 2

**Input:**

```plain
codeforces
atcoder
```

**Output:**

```plain
6
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
t = input()
count = 0
slen = len(s)
tlen = len(t)
startfrom = 0
mincount = 1000
while(startfrom!=(slen-tlen+1)):
    j = startfrom
    for i in range(tlen):
        if t[i]!=s[j]:
            count+=1
        j+=1
    if count < mincount:
        mincount = count
    count = 0
    startfrom+=1
print(mincount,end="")
```
