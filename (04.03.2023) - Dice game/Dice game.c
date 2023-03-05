Problem Statement
Is it possible to get a sum of B when throwing a die with six faces 1, 2, …, 6 A times?
Input
The input consists of two space-separated integers.
A B

Constraints
1≤A≤100
1≤B≤1000
A and B are integers.
Output
If it is possible to get a sum of B, print Yes; otherwise, print No.
Example
Sample Input 1
2 11
Sample Output 1
Yes

Sample Input 2
2 13
Sample Output 2
No

#include <stdio.h>
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    if(b<=(a*6) && b>=a)
        {printf("Yes");}
    else{printf("No");}
    return 0;
}