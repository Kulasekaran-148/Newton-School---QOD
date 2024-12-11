# Table of Contents

- [Problem Description](#problem-description)
- [Input / Expected Output](#input-expected-output)
- [Intuition](#intuition)
- [Complexity Analysis](#complexity-analysis)
- [Solution](#solution)

## Problem Description

You are given integers **L**, **R**, and a string **S** consisting of lowercase English letters. The task is to reverse the order of the **L-th** through **R-th** characters in the string and print the modified string.

### Constraints

- **S** consists of lowercase English letters.
- $( 1 \leq |S| \leq 10^5 )$ where |S| is the length of S
- **L** and **R** are integers.
- $( 1 \leq L \leq R \leq |S| )$

## Input / Expected Output

### Input

The input consists of two lines:

1. The first line contains integers **L** and **R** separated by a space.
2. The second line contains the string **S**.

### Output

Print the string after reversing the order of the **L-th** through **R-th** characters.

### Example 1

**Input:**

```plain
3 7
abcdefgh
```

**Output:**

```plain
abgfedch
```

### Example 2

**Input:**

```plain
1 7
reviver
```

**Output:**

```plain
reviver
```

### Example 3

**Input:**

```plain
4 13
merrychristmas
```

**Output:**

```plain
meramtsirhcyrs
```

## Intuition

1. Split the string into three parts:
   - The part before the **L-th** character.
   - The part between the **L-th** and **R-th** characters (inclusive).
   - The part after the **R-th** character.
2. Reverse the middle part of the string.
3. Concatenate the three parts together to form the final string.

## Complexity Analysis

### Time Complexity

- Extracting substrings and reversing the middle part takes \( O(R - L + 1) \).
- Concatenation of strings takes \( O(|S|) \).
- Overall, the complexity is \( O(|S|) \).

### Space Complexity

- The space complexity is \( O(|S|) \) as we create new substrings and the result string.

## Solution

Below is the Python code for solving the problem:

```python
# Read input values
l, r = map(int, input().split())
s = input()

# Split the string into three parts
before = s[:l-1]  # Part before the L-th character
middle = s[l-1:r] # Part between L-th and R-th characters (inclusive)
after = s[r:]     # Part after the R-th character

# Reverse the middle part and concatenate
result = before + middle[::-1] + after

# Print the final string
print(result)
```

### Explanation of the Code

1. **Splitting the String:**
   - Use slicing to extract the three parts of the string:
     - `before` contains the characters from the start of the string up to (but not including) the **L-th** character.
     - `middle` contains the characters from the **L-th** to the **R-th** character (inclusive).
     - `after` contains the characters after the **R-th** character.
2. **Reversing the Middle Part:**
   - Use Python's slicing `[::-1]` to reverse the `middle` part.
3. **Concatenation:**
   - Concatenate the three parts to form the final string.
4. **Output:**
   - Print the resulting string.
