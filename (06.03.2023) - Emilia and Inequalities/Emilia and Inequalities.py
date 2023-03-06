Problem Statement
Emilia loves to play with numbers. She is given integers A, B, and C. Determine whether A2 +B2 < C2 holds.
Input
The input consists of three space-separated integers A, B, and C.

Constraints
0 ≤ A ≤ 1000
0 ≤ B ≤ 1000
0 ≤ C ≤ 1000
A, B, and C are integers.
Output
If inequality holds, print Yes; otherwise, print No.
Example
Sample Input 1
2 2 4
Sample Output 1
Yes

Sample Input 2
10 10 10
Sample Output 2
No

Sample Input 3
3 4 5
Sample Output 3
No


a,b,c=map(int,input().split())
if(a**2+b**2<c**2):
    print("Yes",end="")
else:
    print("No",end="")