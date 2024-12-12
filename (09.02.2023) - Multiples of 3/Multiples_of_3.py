n=input()
result=0
k=0
if(True):
    for i in range(len(n)):
        result+=int(n[i])
    if(result%3==0):
        print('0',end="")
        exit()
for i in range(len(n)):
    dig=result%3
    if str(dig) in n:
        result-=dig
        k+=1
    else:
        revstring=n[::-1]
        result=result-int(revstring[i]) 
        k+=1
    if(result%3==0 and result!=0):
        print(k,end="")
        exit()
print("-1",end="")