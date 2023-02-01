Problem Statement
You are given integers L, R, and a string S consisting of lowercase English letters.
Print this string after reversing (the order of) the L-th through R-th characters.
Input
The input line contains L and R separated by space. The next line S
L R
S

Constraints
S consists of lowercase English letters.
1≤ |S| ≤ 10^5 (|S| is the length of S. )
L and R are integers.
1 ≤ L ≤ R ≤ |S|
Output
Print the specified string.
Example
Sample Input 1
3 7
abcdefgh
Sample Output 1
abgfedch

Sample Input 2
1 7
reviver
Sample Output 2
reviver

Sample Input 3
4 13
merrychristmas
Sample Output 3
meramtsirhcyrs

l,r = map(int,input().split())
flag=0
s = input()
s2 = s[::-1]
s2 = s2[len(s)-r:len(s)-l+1]
for i in range(len(s)):
    # if(i!=l-1):
    if(i not in range(l-1,r)):
        print(s[i],end="")
    elif flag==0:
        flag=1
        print(s2,end="")