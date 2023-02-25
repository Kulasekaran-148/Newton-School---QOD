Problem Statement
Newton School Coding Contest usually starts at 21:00 IST and lasts for 100 minutes.
You are given an integer K between 0 and 100 (inclusive). Print the time K minutes after 21:00 in the HH:MM format, where HH denotes the hour on the 24- hour clock and MM denotes the minute. If the hour or the minute has just one digit, append a 0 to the beginning to represent it as a 2- digit integer.
Input
The input consists of a single integer.
K

Constraints
K is an integer between 0 and 100 (inclusive).
Output
Print the time K minutes after 21:00 in the format specified in the Problem Statement.
Example
Sample Input 1
63
Sample Output 1
22:03

Sample Input 2
45
Sample Output 2
21:45

Sample Input 3
100
Sample Output 3
22:40

k = int(input())
if(k<60):
    time="21:00"
    if(k<10):
        print(time[0:2]+":0"+str(int(time[3:])+k),end="")
    else:
        print(time[0:2]+":"+str(int(time[3:])+k),end="")
elif(k==60):
    print("22:00",end="")
else:
    time="22:00"
    if(k-60<10):
        print(time[0:2]+":0"+str(int(time[3:])+k-60),end="")
    else:
        print(time[0:2]+":"+str(int(time[3:])+k-60),end="")