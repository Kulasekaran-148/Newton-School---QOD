#include <stdio.h>
#include <stdlib.h>
int main() {
    int n,m,i,waysn=0,waysm=0;
    scanf("%d%d",&n,&m);
    for(i=n-1;i>0;i--)
    {
        waysn=waysn+i;
    }
    for(i=m-1;i>0;i--)
    {
        waysm=waysm+i;
    }
    printf("%d",waysn+waysm);
    return 0;
}