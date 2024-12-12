n=int(input())
input_string=input()
cards=input_string.split()
cards=[int(i) for i in cards]
hashtable=[0 for i in range(n)]
for i in range(4*n-1):
    hashtable[cards[i]-1]+=1
print(hashtable.index(3)+1,end="")