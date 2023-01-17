#include <stdio.h>
#include <stdlib.h>
int main() {
    int n,flag=1,i;
    scanf("%d",&n);
    if(n==2 || n==3)
    {
        printf("%d",n);
    }
    else if(flag==1)
    {
    for(i=2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                // printf("Hello");
                flag=0;
                n++;
                break;
            }
            else if(i==n/2)
            {
                // printf("Whats up");
                printf("%d",n);
            }
        }
    }
    if(flag==0)
    {
        // printf("\nNice");
        for(i=2;i<=n/2;i++)
        {
            if(n%i==0)
            {
                // printf("\nGood day[%d][%d]",i,n);
                n++;
                i=1;
            }
            else if(i==((n/2)))
            {
                // printf("\nProgram[%d][%d]",i,n);
                printf("%d",n);
            }
        }
    }
    return 0;
}