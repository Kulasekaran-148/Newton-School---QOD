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