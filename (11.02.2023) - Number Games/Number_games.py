n,k = map(int, input().split())
for i in range(k):
    if n%200==0:
        n/=200
        n=int(n)
        # print(i,n)
    else:
        n=str(n)
        n+="200"
        n=int(n)
        # print(i,n)
print(n,end="")