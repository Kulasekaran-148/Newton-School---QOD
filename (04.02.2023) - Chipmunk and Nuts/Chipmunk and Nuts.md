# Table of Contents

- [Problem Description](#problem-description)
- [Input](#input)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

There are N trees. The $i^{th}$ tree bears $A_i$ nuts. Chipmunk will harvest nuts from the trees in the following manner:

- From a tree with 10 or fewer nuts, she does not take nuts.
- From a tree with more than 10 nuts, she takes all but 10 nuts.
- Find the total number of nuts Chipmunk will take from the trees.

### Constraints

- $1 \leq N \leq 1000$
- $0 \leq A_i \leq 1000$
- All values in the input are integers

## Input

Input is given from Standard Input in the following format:

- N
- $A_1… A_N$

### Example 1

**Input:**

```plain
3
6 17 28
```

**Output:**

```plain
25
```

### Example 2

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

```C
int main()
{   
    int n,i,result=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
        if(arr[i]>=10)
        {result+=(arr[i]-10);}
        else
        {result+=0;}
    }
    printf("%d",result);
    return 0;
}
```
