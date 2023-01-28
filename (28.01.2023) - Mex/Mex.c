Problem Statement
You are given a sequence of length N consisting of integers:
A=(A1, A2,...., AN)
Find the smallest non-negative integer not in (A1, A2,....,AN).
Input
The input contains N and elements of sequence separated by a new line.
N
A1, A2,. , AN

Constraints
1≤N≤2000
0≤Ai≤2000
All values in the input are integers.
Output
Print the answer.
Example
Sample Input 1
8
0 3 2 6 2 1 0 0
Sample Output 1
4

Sample Input 2
3
2000 2000 2000
Sample Output 2
0

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int n,i,min=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        if(min==arr[i])
        {
            min++;
            i=0;
        }
    }
    printf("%d",min);
    return 0;
}