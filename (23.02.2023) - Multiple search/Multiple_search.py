Problem Statement
Print a number between A and B (inclusive) that is a multiple of C. If such numbers exist, print the minimum among them. If there is no such number, print -1.
Input
The input contains three space separated integers.
A B C

Constraints
0≤X≤1000
All values in input are integers.
Output
Print the answer.
If there is no number with the desired property, print -1.
Example
Sample Input 1
123 456 100
Sample Output 1
200

Sample Input 2
630 940 314
Sample Output 2
-1

a,b,c = map(int, input().split())
k=0
flag=0
while(c*k<=b and c!=0):
    if(c*k>=a):
        print(c*k,end="")
        flag=1
        break
    k+=1
if(flag==0):
    print(-1,end="")