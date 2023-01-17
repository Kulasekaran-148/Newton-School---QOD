#include <stdio.h>
#include <stdlib.h>
int main() {
    int count,weights[100],i,j=0,bal1=0,bal2=0,temp=100;
    scanf("%d",&count);
    for(i=0;i<count;i++)
    {
        scanf("%d",&weights[i]);
    }
    for(i=0;i<count;i++)
    {
        for(j=0;j<count;j++)
        {
            if(i>=j)
            {
                bal1=bal1+weights[j];
                // printf("\nIteration[%d]Bal1=%d",i,bal1);
            }
            else
            {
                bal2=bal2+weights[j];
                // printf("\nIteration[%d]Bal2=%d",i,bal2);
            }
        }
        if(bal1>bal2)
        {
            if((bal1-bal2)<temp){
                temp=(bal1-bal2);
            }
        }
        else
        {
            if((bal2-bal1)<temp){
                temp=(bal2-bal1);
            }
        }
        bal1=0;
        bal2=0;
    }
    printf("%d",temp);
}