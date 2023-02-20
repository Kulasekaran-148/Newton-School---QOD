Problem Statement
Let xyz denote the 3- digit integer whose digits are x, y, and z from left to right.
Given a 3-digit integer, abc none of whose digits is 0, find abc+bca+cab.
Input
The input is given as follows.
abc

Constraints
abc is a 3- digit integer, none of whose digits is 0.
Output
Print the answer.
Example
Sample Input 1
123
Sample Output 1
666

Sample Input 2
999
Sample Output 2
2997

n=int(input())
a=n
arr=[0 for i in range(3)]
i=2
while(a!=0):
    arr[i]=a%10
    a=int(a/10)
    i-=1
result=(arr[0]*100+arr[1]*10+arr[2]+arr[1]*100+arr[2]*10+arr[0]+arr[2]*100+arr[0]*10+arr[1])
print(result,end="")