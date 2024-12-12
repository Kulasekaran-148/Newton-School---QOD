# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

We have $4$ cards with an integer $1$ written on it, $4$ cards with $2$, …, 4 cards with $N$, for a total of $4N$ cards.

Alexa shuffled these cards, removed one of them, and gave you a pile of the remaining $4N − 1$ cards. The $i^{th}$ card $(1 \leq i \leq 4N−1)$ of the pile has an integer $A_i$ written on it.

Find the integer written on the card removed by Alexa.

### Constraints

- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- $1 \leq i \leq 4N−1$
- For each $k(1 \leq k \leq N)$, there are at most $4$ indices $i$ such that $A_i=k$.
- All values in input are integers.

## Input

The first line of input contains an integer N.
The second line contains N space separated integers as follows:

```plain
N
A1 A2 ... AN
```

### Example 1

**Input:**

```plain
3
1 3 2 3 3 2 2 1 1 1 2
```

**Output:**

```plain
3
```

### Example 2

**Input:**

```plain
1
1 1 1
```

**Output:**

```plain
1
```

### Example 3

**Input:**

```plain
4
3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
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
n=int(input())
input_string=input()
cards=input_string.split()
cards=[int(i) for i in cards]
hashtable=[0 for i in range(n)]
for i in range(4*n-1):
    hashtable[cards[i]-1]+=1
print(hashtable.index(3)+1,end="")
```
