Problem Statement
You are given two strings S and T consisting of lowercase English letters. Determine if S is a prefix of T.
Input
The input contains two strings separated by a new line.
S
T

Constraints
S and T are strings of lengths between 1 and 100 (inclusive) consisting of lowercase English letters.
Output
Print "Yes" if S is a prefix of T, "No" otherwise.

Note: that the judge is case-sensitive.
Example
Sample Input 1
new
newton
Sample Output 1
Yes

Sample Input 2
ewt
newton
Sample Output 2
No

Sample Input 3
aaaa
aa
Sample Output 3
No

s = input()
t = input()
flag=0
if(len(s)<len(t)):
    for i in range(len(s)):
        if s[i]==t[i]:
            pass
        else:
            print("No")
            flag=1
            break
    if flag==0:
        print("Yes")
else:
    print("No")