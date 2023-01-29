Problem Statement
Alexa loves to play with strings. She is given a string S consisting of lowercase English letters.
If 'a' appears in S, print the last index at which it appears; otherwise, print −1. (The index starts at 1. )
Input
The input contains only one string.
S

Constraints
1 <= |S| <= 100
Output
Print the answer.
Example
Sample Input 1
abcdaxayz
Sample Output 1
7

Sample Input 2
bcbbbz
Sample Output 2
-1


s = input()
flag=0
for i in range(len(s)):
    if "a" == s[i]:
        result = i
        flag=1
if flag:
    print(result+1)
else:
    print("-1")