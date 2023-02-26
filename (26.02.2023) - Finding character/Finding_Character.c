Problem Statement
Find the X- th character from the beginning of the string that is obtained by concatenating these characters: N copies of A's, N copies of B's, …, and N copies of Z's, in this order.
Input
The input consists of two space separated integers.
N X

Constraints
1≤N≤100
1≤X≤N≤26
All values in input are integers.
Output
Print the answer.
Example
Sample Input 1
1 3
Sample Output 1
C

Sample Input 2
2 12
Sample Output 2
F

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int n,x;
    scanf("%d %d",&n,&x);
    char str[n*26],letter;
    int k=0;
    for(letter='A';letter<='Z';letter++)
    {
        for(int j=0;j<n;j++)
        {
            str[k]=letter;
            k++;
        }
    }
    printf("%c",str[x-1]);
    return 0;
}