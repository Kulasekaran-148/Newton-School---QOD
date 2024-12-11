l,r = map(int,input().split())
flag=0
s = input()
s2 = s[::-1]
s2 = s2[len(s)-r:len(s)-l+1]
for i in range(len(s)):
    # if(i!=l-1):
    if(i not in range(l-1,r)):
        print(s[i],end="")
    elif flag==0:
        flag=1
        print(s2,end="")