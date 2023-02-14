Problem Statement
Having learned the multiplication table, Alexa can multiply two integers between 1 and 9 (inclusive) together. Given an integer N, determine whether N can be represented as the product of two integers between 1 and 9. If it can, print Yes; if it cannot, print No.
Input
The input consists of a single integer.
N

Constraints
1≤N≤100
Output
If N can be represented as the product of two integers between 1 and 9 (inclusive), print Yes; if it cannot, print No.
Example
Sample Input 1
10
Sample Output 1
Yes

Sample Input 2
50
Sample Output 2
No

Sample Input 3
81
Sample Output 3
Yes

n = int(input())
flag=0
for i in range(1,9):
    if n/i in [1,2,3,4,5,6,7,8,9]:
        print("Yes",end="")
        flag=1
        break
if(flag==0):
    print("No",end="")