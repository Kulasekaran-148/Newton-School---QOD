Problem Statement
Bob challenged Alexa with a puzzle. He asked her to count how many integers not less than
A and not more than B are there? Help Alexa to win.
Input
The input consists of two space separated integers.
A B

Constraints
1≤A≤100
1≤B≤100
A and B are integers.
Output
Print the number of integers not less than A and not more than B.
Example
Sample Input 1
2 4
Sample Output 1
3

Sample Input 2
10 100
Sample Output 2
91

Sample Input 3
3 2
Sample Output 3
0

a,b = map(int,input().split())
if(a<b):
    print(b-a+1, end="")
else:
    print(0, end="")