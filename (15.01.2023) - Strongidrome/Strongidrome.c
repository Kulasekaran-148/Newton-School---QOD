#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int main() {
    bool flag1=false,flag2=false,flag3=false;
    char str1[100];
    int i,len4;
    scanf("%s",str1);
    len4 = strlen(str1)-((strlen(str1)+3)/2)+1;
    char str2[strlen(str1)],str3[strlen(str1)/2], str4[len4];
    for(i=0;i<strlen(str1);i++)
    {
        str2[i]=str1[strlen(str1)-1-i];
    }
    for(i=0;i<strlen(str1);i++)
    {
        if(str1[i]!=str2[i])
        {
            flag2=false;
            break;
        }
        else
        {
            flag1=true;
        }
    }
    // printf("Flag1 is %d\n",flag1);
    if(flag1==true)
    {
        for(i=0;i<(strlen(str1)/2);i++)
        {
            str3[i]=str2[(strlen(str1)/2)-1-i];
        }
        // printf("Str3 is %s\n",str3);
        for(i=0;i<(strlen(str1)/2);i++)
        {
            if(str3[i]!=str2[i])
            {
                flag2=false;
                break;
            }
            else
            {
                flag2=true;
            }
        }
        if(flag2==true)
        {
            for(i=0;i<=len4;i++)
            {
                str4[i]=str1[strlen(str1)-1-i];
            }
            // printf("Str4 is %s\n",str4);
            for(i=0;i<=len4;i++)
            {
                if(str4[i]!=str1[i])
                {
                    flag3=false;
                    break;
                }
                else
                {
                    flag3=true;
                }
            }
        }
    }
    // printf("Flag2 is %d\n",flag2);
    
    if(flag1==true && flag2==true && flag3==true)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }
    return 0;
}