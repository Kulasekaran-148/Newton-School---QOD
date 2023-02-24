Problem Statement
We have five cards with integers A, B, C, D, and E written on them, one on each card.

This set of five cards is called a Full house if and only if the following below condition is satisfied:
1. Any three cards with the same number written on them
2. Rest two cards with the same numbers written on them.

Determine whether the set is a Full house.
Input
The input consists of 5 space separated integers.
A B C D E

Constraints
1≤A, B, C, D, E≤13
Not all of A, B, C, D, and E are the same.
All values in input are integers.
Output
If the set is a Full house, print Yes; otherwise, print No.
Example
Sample Input 1
1 2 1 2 1
Sample Output 1
Yes

Sample Input 2
12 12 11 1 2
Sample Output 2
No

arr = list(map(int,input().split()))
occ_arr = [0 for i in range(5)]
for j in range(5):
    for i in range(5):
        if arr[j]==arr[i]:
            occ_arr[j]+=1
if(3 in occ_arr and 2 in occ_arr):
    print("Yes",end="")
else:
    print("No",end="")