a,b = map(int,input().split())
sum1=0
sum2=0
while(a>0):
    sum1+=a%10
    a/=10
    sum2+=b%10
    b/=10
    sum1=int(sum1)
    sum2=int(sum2)
print(max(sum1,sum2),end="")