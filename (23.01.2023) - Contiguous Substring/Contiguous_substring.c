#include <stdio.h>
#include <stdlib.h>
#include<string.h>

void removeChar(char *str, int n) {
    int i;
    for (i = n; i < strlen(str) - 1; i++) {
        str[i] = str[i + 1];
    }
    str[i] = '\0';
}
int main() {
    char s[100],t[100];
    scanf("%s %s",s,t);
    if(!strcmp(s,t))
    {
        printf("Yes");
    }
    else if(strstr(s,t))
    {

        printf("Yes");
    }
    else
    {
        printf("No");
    }
    return 0;
}