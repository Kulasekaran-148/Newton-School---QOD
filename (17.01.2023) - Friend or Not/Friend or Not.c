#include <stdio.h>
#include <stdlib.h>
int main() {
    int n,i,c_Value,count=1,a,b,c,d,limit;
    scanf("%d",&n);
    limit=2*(n-1);
    for(i=0;i<limit;)
    {
        if(i==0)
        {
            scanf("%d %d %d %d",&a,&b,&c,&d);
            if(a==c || b==c)
                {c_Value=c;count++;}
            else if(a==d || b==d)
                {c_Value=d;count++;}
            else {count=1; a=c; b=d;}
        i+=4;
        }
        else
        {
        scanf("%d %d",&c,&d);i+=2;
        if((a==c || b==c) && c_Value==c)    
            {c_Value=c;count++;}
        else if((a==d || b==d) && c_Value==d)
            {c_Value=d;count++;}
        else {count=1; a=c; b=d;}
        } 
    }
    if(count==(n-1)){printf("Yes");}
    else {printf("No");}
}