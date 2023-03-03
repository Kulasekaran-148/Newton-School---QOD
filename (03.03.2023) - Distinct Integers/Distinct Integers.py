Problem Statement
Emilia loves to play with integers. Print how many distinct integers there are in given five integers
A, B, C, D, and E.
Input
The input consists of 5 space-separated integers.
A B C D E

Constraints
0 ≤ A, B, C, D, E ≤ 100
All values in the input are integers.
Output
Print the answer.
Example
Sample Input 1
31 9 24 31 24

Sample Output 1
3

Sample Input 2
0 0 0 0 0

Sample Output 2
1
a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
print(len(b),end="")