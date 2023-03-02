Problem Statement
Rohit loves to play with balls. He removed A balls from a box that contained N balls and then put B new balls into that box. How many balls does the box contain now?
Input
The input consists of 3 space separated integers.
N A B

Constraints
All values in input are integers.
100≤N≤200
1≤A, B≤100
Output
Print the answer as an integer.
Example
Sample Input 1
100 1 2
Sample Output 1
101

Sample Input 2
100 2 1
Sample Output 2
99

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int n,a,b;
    scanf("%d %d %d",&n,&a,&b);
    printf("%d",n-a+b);
    return 0;
}