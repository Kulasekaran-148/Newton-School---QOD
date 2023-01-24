#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
    signed int goal,wall,hammer;
    scanf("%d %d %d",&goal,&wall,&hammer);
    if((goal>0 && wall>goal) || (goal<0 && wall<goal) || (goal>0 && wall<0) || (goal<0 && wall>0)) //bob goal wall or //wall goal bob
        {printf("%d",abs(goal));}
    else if(goal>0 && wall<goal && wall>0) //bob wall goal
        {
            if(hammer<0)//hammer bob wall goal
                {printf("%d",(2*abs(hammer))+goal);}
            else if(hammer<wall)//bob hammer wall goal
                {printf("%d",goal);}
            else
                {printf("-1");}
        }
    else if(goal<0 && wall>goal && wall<0)//goal wall bob
        {
            if(hammer>0)
                {printf("%d",(2*abs(hammer)+abs(goal)));}
            else if(hammer>wall)
                {printf("%d",abs(goal));}
            else
                {printf("-1");}
        }
    return 0;
}