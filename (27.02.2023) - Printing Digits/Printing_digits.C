Problem Statement
You are given an integer N of at least 100. Print the last two digits of N. Strictly speaking, print the tens and one's digits of N in this order.
Input
The input consists of an integer.
N

Constraints
100≤N≤999
N is an integer.
Output
Print the answer.
Example
Sample Input 1
254
Sample Output 1
54

Sample Input 2
101
Sample Output 2
01

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int n,k,t;
    scanf("%d",&n);
    k=n/100;
    t=n%(k*100);
    if((t/10)==0)
    {
        printf("0%d",t);
    }
    else
    {
        printf("%d",t);
    }
    return 0;
}