#include<stdio.h>
#include<string.h>
int main()
{
    int a,b,c,result;
    scanf("%d%d%d",&a,&b,&c);
    if(a<b && a<c)
    {
        result=result+a;
        if(b<c)
        {
            result=result+b;
        }
        else{
            result=result+c;
        }
    }
    else if(b<a && b<c)
    {
        result=result+b;
        if(a<c)
        {
            result=result+a;
        }
        else
        {
            result=result+c;
        }
    }
    else
    {
        result=result+c;
        if(a<b)
        {
            result=result+a;
        }
        else
        {
            result=result+b;
        }
    }
    printf("%d",result);
}