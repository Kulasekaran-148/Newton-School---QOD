#include <stdio.h>
int main() {
    int a,b;
    scanf("%d %d",&a,&b);
    if(b<=(a*6) && b>=a)
        {printf("Yes");}
    else{printf("No");}
    return 0;
}