a,b,c,k = map(int,input().split())
result=0;
if(k>=a):
    result+=a
    k-=a
else:
    result+=k*1
    k=0
if(k>=b):
    k-=b
elif(k>0):
    result-=k*b
    k=0
if(k>=c):
    result-=c
    k-=c
    k=0
elif(k>0):
    result-=k*(1)
print(result,end="")