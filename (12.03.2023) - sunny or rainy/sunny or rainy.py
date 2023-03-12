Problem Statement
You are given a string S, which represents a weather forecast for the seven days starting tomorrow.
The ith of those seven days is forecast to be sunny if the ith character of S is o, and rainy if that character is x. Tell us whether the Nth day is forecast to be sunny.
Input
The first line of the input consists of an integer N.
The second line of the input consists of a string.

Constraints
N is an integer between 1 and 7 (inclusive).
S is a string of length 7 consisting of o and x.
Output
Print Yes if the N- th of the seven days starting tomorrow is forecast to be sunny, and No if that day is forecast to be rainy.
Example
Sample Input 1
4
oooxoox
Sample Output 1
No

Sample Input 2
7
ooooooo
Sample Output 2
Yes

n = int(input())
s = input()
if(s[n-1]=='o'):
    print('Yes',end="")
else:
    print('No',end="")