Problem Statement
Let S(n) denote the sum of the digits in the decimal notation of n. For example, S(101)=1+0+1=2.
Given an integer N, determine if S(N) divides N.
Input
The input consists of a single integer.
N

Constraints
1≤N≤10^9
Output
If S(N) divides N, print Yes; if it does not, print No.
Example
Sample Input 1
12
Sample Output 1
Yes

Sample Input 2
101
Sample Output 2
No

Sample Input 3
999999999
Sample Output 3
Yes

n=int(input())
dig=n
result=0
while(dig>0):
    a=dig%10
    result+=a
    dig/=10
    dig=int(dig)
# print(result)
if(n%int(result)==0):
    print("Yes",end="")
else:
    print("No",end="")