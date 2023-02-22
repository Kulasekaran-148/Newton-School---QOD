Problem Statement
You are given an integer N between 0 and 9999 (inclusive).
Print it as a four-digit string after appending the necessary number of leading zeros.
Input
The input consists of a single integer.
N

Constraints
0≤N≤9999
N is an integer.
Output
Print the four digit string after appending to it the necessary number of leading zeros.
Example
Sample Input 1
321
Sample Output 1
0321

Sample Input 2
7777
Sample Output 2
7777

n=input()
if (len(n)==4): print(n,end="")
else: 
    s=[0 for i in range(4-len(n))]
    for i in s:
        print(str(i),end="")
    print(n,end="")