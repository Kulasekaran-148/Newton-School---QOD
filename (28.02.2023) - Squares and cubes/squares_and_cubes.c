Problem Statement
Bob is given an integer a. He wants to find the value of a + a^2 + a^3.
Input
The input consists of an integer a.

Constraints
1≤a≤10
a is an integer.
Output
Print the answer.
Example
Sample Input 1
2
Sample Output 1
14

Sample Input 2
10
Sample Output 2
1110

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library
int main() {
    int a;
    scanf("%d",&a);
    printf("%d",a+a*a+a*a*a);
    return 0;
}