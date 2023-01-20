#include <stdio.h>
int main() {
    int s, t, a, b, c, ways=0;
    scanf("%d %d",&s,&t);
    for(a=0;a<=s;a++)
    {
        for(b=0;b<=s;b++)
        {
            for(c=0;c<=s;c++)
            {
                if((a+b+c)<=s && (a*b*c)<=t)
                {
                    ways+=1;
                }   
            }
        }
    }
    printf("%d",ways);
}