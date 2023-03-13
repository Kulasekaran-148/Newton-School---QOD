Problem Statement
You are given a string S consisting of lowercase English characters. The length of S is between 1 and 3, inclusive. Print the string of length 6 that is a repetition of S.
It can be shown that there uniquely exists such a string under the Constraints of this problem.
Input
The input consists of a string S.

Constraints
S is a string consisting of lowercase English characters of length between 1 and 3, inclusive.
Output
Print the answer string, which is of length 6.
Example
Sample Input 1
abc
Sample Output 1
abcabc

Sample Input 2
zz
Sample Output 2
zzzzzz

s = input()
length = len(s)
for i in range (int(6/length)):
    print(s,end="")