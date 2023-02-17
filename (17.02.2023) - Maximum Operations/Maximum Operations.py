Problem Statement
There are N positive integers written on a blackboard: A1,. , AN.
Edward can perform the following operation when all integers on the blackboard are even:

Replace each integer X on the blackboard by X divided by 2.
Find the maximum possible number of operations that Edward can perform.
Input
The input consists of an integer N and N space separated integers.
N
A1 A2. . AN

Constraints
1≤N≤200
1≤Ai≤10^9
Output
Print the maximum possible number of operations that Edward can perform.
Example
Sample Input 1
3
8 12 40
Sample Output 1
2

Sample Input 2
4
5 6 8 10
Sample Output 2
0

n = int(input())
numbers = input().split()
numbers = list(map(int,numbers))
count = 0
flag = 1
evencount = 0
while(flag):
    for i in range(len(numbers)):
        if(numbers[i]%2==0):
            numbers[i]/=2
            numbers[i] = int(numbers[i])
            evencount+=1
    if(evencount == len(numbers)):
        count+=1
        evencount = 0
    else:
        flag = 0
        break
print(count,end="")