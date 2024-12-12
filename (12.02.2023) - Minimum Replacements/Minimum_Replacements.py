s = input()
t = input()
count = 0
slen = len(s)
tlen = len(t)
startfrom = 0
mincount = 1000
while(startfrom!=(slen-tlen+1)):
    j = startfrom
    for i in range(tlen):
        if t[i]!=s[j]:
            count+=1
        j+=1
    if count < mincount:
        mincount = count
    count = 0
    startfrom+=1
print(mincount,end="")