Problem Statement
We have A cards, each of which has an integer 1 written on it. Similarly, we also have B cards with 0s and C cards with −1s.
We will pick up K among these cards. What is the maximum possible sum of the numbers written on the cards chosen?
Input
The input consists of 4 space separated integers as follows :
A B C K

Constraints
All values in input are integers.
0≤A, B, C
1≤K≤A+B+C≤2×10^9
Output
Print the maximum possible sum of the numbers written on the cards chosen.
Example
Sample Input 1
2 1 1 3
Sample Output 1
2

Sample Input 2
1 2 3 4
Sample Output 2
0

Sample Input 3
2000000000 0 0 2000000000
Sample Output 3
2000000000

a,b,c,k = map(int,input().split())
result=0;
if(k>=a):
    result+=a
    k-=a
else:
    result+=k*1
    k=0
if(k>=b):
    k-=b
elif(k>0):
    result-=k*b
    k=0
if(k>=c):
    result-=c
    k-=c
    k=0
elif(k>0):
    result-=k*(1)
print(result,end="")