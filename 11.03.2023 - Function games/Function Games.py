Problem Statement
Let us define a function f as f(x)=x2+2x+3. Given an integer t, find f(f(f(t)+t)+f(f(t))).
Here, it is guaranteed that the answer is an integer not greater than 2×109.
Input
The input consists of a single integer.

Constraints
t is an integer between 0 and 10 (inclusive).
Output
Print the answer as an integer.
Example
Sample Input 1
0
Sample Output 1
1371

Sample Input 2
3
Sample Output 2
722502

t = int(input())
def f(t):
    return t**2 + 2*t + 3
print( f(f(f(t)+t)+f(f(t))) , end="")