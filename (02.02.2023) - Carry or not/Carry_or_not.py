
Problem Statement
You are given positive integers A and B.
Let us calculate A+B (in decimal). If it does not involve a carry, print Easy; if it does, print Hard.
Input
The input contains two space separated numbers:
A B

Constraints
A and B are integers.
1 ≤ A, B ≤ 10^18
Output
If the calculation does not involve a carry, print Easy; if it does, print Hard.
Example
Sample Input 1
229 390
Sample Output 1
Hard

Sample Input 2
123456789 9876543210
Sample Output 2
Easy

a,b = map(str, input().split())
flag=0
while(len(a)>len(b)):
    b="0"+b
while(len(b)>len(a)):
    a="0"+a
a=a[::-1]
b=b[::-1]
for i in range(len(a)):
    if(int(a[i])+int(b[i]))<10:
        pass
    else:
        print("Hard",end="")
        flag=1
        break
if flag==0:
    print("Easy",end="")