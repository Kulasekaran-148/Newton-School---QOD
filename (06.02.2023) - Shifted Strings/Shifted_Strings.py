Problem Statement
We have a string S consisting of uppercase English letters. Additionally, an integer N will be given.
Shift each character of S by N in alphabetical order (see below), and print the resulting string.

We assume that A follows Z. For example, shifting A by 2 results in C (A → B → C), and shifting Y by 3 results in B (Y → Z → A → B).
Input
The input contains a number and a string separated by a new line.

N
S
Output
Print the string resulting from shifting each character of S by N in alphabetical order
Example
Sample Input 1
2
ABCXYZ
Sample Output 1
CDEZAB

Sample Input 2
0
ABCXYZ
Sample Output 2
ABCXYZ

Sample Input 3
13
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Sample Output 3
NOPQRSTUVWXYZABCDEFGHIJKLM

n=int(input())
n=n%26
s=input()

def shift_alphabet(s, n):
    result = ""
    n = n % 26
    for char in s:
        if char.isalpha() and char.isupper():
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            result += char
    return result
print(shift_alphabet(s,n))