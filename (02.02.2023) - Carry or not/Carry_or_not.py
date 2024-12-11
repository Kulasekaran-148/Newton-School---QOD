a,b = map(str, input().split())
flag=0
while(len(a)>len(b)):
    b="0"+b
while(len(b)>len(a)):
    a="0"+a
a=a[::-1]
b=b[::-1]
for i in range(len(a)):
    if(int(a[i])+int(b[i]))<10:
        pass
    else:
        print("Hard",end="")
        flag=1
        break
if flag==0:
    print("Easy",end="")