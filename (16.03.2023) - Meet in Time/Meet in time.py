Problem Statement
Alexa is meeting up with Bob. They have planned to meet at a place that is D meters away from Alexa's house in T minutes from now. Alexa will leave her house now and go straight to the place at a speed of
S meters per minute. Will she arrive in time?
Input
The input consists of three space separated integers.
D T S

Constraints
1 ≤ D ≤ 10000
1 ≤ T ≤ 10000
1 ≤ S ≤10000
All values in input are integers.
Output
If Alexa will reach the place in time, print Yes; otherwise, print No.
Example
Sample Input 1
1000 15 80
Sample Output 1
Yes

Sample Input 2
2000 20 100
Sample Output 2
Yes

Sample Input 3
10000 1 1
Sample Output 3
No

d,t,s = map(int,input().split())
if(d/s<=t):
    print("Yes",end="")
else:
    print("No",end="")