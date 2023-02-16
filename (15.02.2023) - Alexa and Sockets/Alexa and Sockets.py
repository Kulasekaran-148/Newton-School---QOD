Problem Statement
Alexa's house has only one socket.
Alexa wants to extend it with some number of power strips, each with A sockets, into B or more empty sockets. One power strip with A sockets can extend one empty socket into A empty sockets.
Find the minimum number of power strips required.
Input
The input consists of two space separated integers.
A B

Constraints
All values in input are integers.
2≤A≤20
1≤B≤20
Output
Print the minimum number of power strips required.
Example
Sample Input 1
4 10
Sample Output 1
3

Sample Input 2
8 9
Sample Output 2
2

Sample Input 3
8 8
Sample Output 3
1

a,b = map(int,input().split())
sockets = 0
req = 0
if(b==1):
    print(req,end="")
    exit()
while(sockets<b):
    if(sockets==0):
        req+=1
        sockets=a
    else:
        req+=1
        sockets=sockets-1+a
print(req,end="")