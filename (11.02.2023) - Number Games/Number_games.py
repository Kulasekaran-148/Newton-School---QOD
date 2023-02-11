Problem Statement
You are given an integer N. Do the following operation K times on it and print the resulting integer.
If N is a multiple of 200, divide it by 200. Otherwise, see N as a string and append 200 to the end of it.
For example, 7 would become 7200, and 1234 would become 1234200.
Input
The input consists of two space separated integers as follows:
N K

Constraints
All values in input are integers.
1≤N≤10^5
1≤K≤20
Output
Print the answer as an integer.
Example
Sample Input 1
2021 4
Sample Output 1
50531

Sample Input 2
40000 2
Sample Output 2
1

Sample Input 3
8691 20
Sample Output 3
84875488281

n,k = map(int, input().split())
for i in range(k):
    if n%200==0:
        n/=200
        n=int(n)
        # print(i,n)
    else:
        n=str(n)
        n+="200"
        n=int(n)
        # print(i,n)
print(n,end="")