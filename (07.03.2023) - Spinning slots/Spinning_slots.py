Problem Statement
Edward is playing the slots. The result of a spin is represented by three uppercase English letters
C1, C2, and C3. It is considered a win when all of them are the same letter.
Determine whether Edward will win or not.
Input
The input consists of a string S.

Constraints
S consists of 3 characters all of which are uppercase English letters.
Output
If the result is a win, print Won; otherwise, print Lost.
Example
Sample Input 1
SSS
Sample Output 1
Won

Sample Input 2
WVW
Sample Output 2
Lost

s1 = input()
if(s1[0]==s1[1] and s1[0]==s1[2]):
    print("Won",end="")
else:
    print("Lost",end="")