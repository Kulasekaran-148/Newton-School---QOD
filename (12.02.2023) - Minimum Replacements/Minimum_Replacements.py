Problem Statement
Given are two strings S and T.
Let us change some of the characters in S so that T will be a substring of S.
At least how many characters do we need to change?

Here, a substring is a consecutive subsequence. For example, xxx is a substring of yxxxy, but not a substring of xxyxx.
Input
The input consists of two strings separated by a line.
S
T

Constraints
1 <= |S|, |T| <= 1000
S and T consist of lowercase English letters.
Output
Print the minimum number of characters in S that need to be changed.
Example
Sample Input 1
cabacc
abc
Sample Output 1
1

Sample Input 2
codeforces
atcoder
Sample Output 2
6

s = input()
t = input()
count = 0
slen = len(s)
tlen = len(t)
startfrom = 0
mincount = 1000
while(startfrom!=(slen-tlen+1)):
    j = startfrom
    for i in range(tlen):
        if t[i]!=s[j]:
            count+=1
        j+=1
    if count < mincount:
        mincount = count
    count = 0
    startfrom+=1
print(mincount,end="")