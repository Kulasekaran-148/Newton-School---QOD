Problem Statement
You are given a string S ending with er or ist.
If S ends with er, print er; if it ends with ist, print ist.
Input
The input consists of a string.
S

Constraints
2≤∣S∣≤20
S consists of lowercase English letters.
S ends with er or ist.
Output
Print the answer.
Example
Sample Input 1
coder
Sample Output 1
er

Sample Input 2
tourist
Sample Output 2
ist

Sample Input 3
er
Sample Output 3
er

s = input()
s = s[::-1]
if(s[0]=="r" and s[1]=="e"):
    print("er",end="")
elif(s[0]=="t" and s[1]=="s" and s[2]=="i"):
    print("ist",end="")