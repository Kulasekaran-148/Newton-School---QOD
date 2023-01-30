Problem Statement
There was an exam consisting of three problems worth 1, 2, and 4 points.
Alexa, Edward, and Bob took this exam. Alexa scored A points, and Edward scored B points.

Bob solved all of the problems solved by at least one of Alexa and Edward and failed to solve any of the problems solved by, neither of them.

#Find Bob's score.
#It can be proved that Bob's score is uniquely determined under the Constraints of this problem.

Input
The input contains two integers separated by a space
A B

Constraints
0≤A, B≤7
A and B are integers.
Output
#Print Bob's score as an integer.
Example
Sample Input 1
1 2
Sample Output 1
3

Sample Input 2
5 3
Sample Output 2
7

Sample Input 3
0 0
Sample Output 3
0


a,b=map(int, input().split())
if(a%2==0):
    if(a==0):
        arr1=[0]
    elif(a==2):
        arr1=[2]
    elif(a==4):
        arr1=[4]
    else:
        arr1=[2,4]
else:
    if(a==1):
        arr1=[1]
    elif(a==3):
        arr1=[1,2]
    elif(a==5):
        arr1=[1,4] 
    else:
        print(7,end="")
        exit()
if(b%2==0):
    if(b==0):
        arr2=[0]
    elif(b==2):
        arr2=[2]
    elif(b==4):
        arr2=[4]
    else:
        arr2=[2,4]
else:
    if(b==1):
        arr2=[1]
    elif(b==3):
        arr2=[1,2]
    elif(b==5):
        arr2=[1,4] 
    else:
        print(7,end="")
        exit()
arr3=arr1+arr2
arr3=[*set(arr3)]
print(sum(arr3),end="")