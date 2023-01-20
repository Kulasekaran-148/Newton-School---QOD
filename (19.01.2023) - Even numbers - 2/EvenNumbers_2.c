#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int signed n,m,i,count=0;
    scanf("%d %d",&n,&m);
    // printf("%d %d\n",n,m);
    for(i=n;i<m && count<5;i++)
    {
        if(i!=n && i!=m && i%2==0)
        {
            printf("%d ",i);
            count++;
        }
    }
    return 0;
}