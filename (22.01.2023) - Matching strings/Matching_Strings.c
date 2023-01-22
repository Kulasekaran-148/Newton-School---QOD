#include <stdio.h>
#include <string.h>
int main() {
    int i,match;
    char s[100],t[100],temp;
    scanf("%s %s",s,t);
    
    match=strcmp(s,t);
    if(match==0)
    {
        printf("Yes");
    }
    else
    {
         for(i=0;i<strlen(s);i++)
         {
             if(s[i]!=t[i] && s[i+1]==t[i])
             {
                 temp=t[i];
                 t[i]=t[i+1];
                 t[i+1]=temp;
                 break;
             }
         }
         match=strcmp(s,t);
         {
             if(match==0)
             {
                 printf("Yes");
             }
             else
             {
                 printf("No");
             }
         }
    }
    return 0;
}