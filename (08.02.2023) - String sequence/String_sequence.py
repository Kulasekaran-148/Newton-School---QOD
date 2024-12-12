seq=input().split()
seq=[int(i) for i in seq]
for i in range(26):
    print(chr(ord('a')-1+seq[i]),end="")