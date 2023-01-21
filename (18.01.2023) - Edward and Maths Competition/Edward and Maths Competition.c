#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library
#include <math.h>

int main() {
    int n;
    scanf("%d",&n);
    if(n%2==0)
    {
        printf("%d",(n/2)*(n/2));
    }
    else
    {
        printf("%d",((n/2)+1)*(n/2));
    }
    return 0;
}