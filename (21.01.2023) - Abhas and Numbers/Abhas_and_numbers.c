#include <stdio.h>
#include <math.h>
int main() {
    long n,k;
    scanf("%ld %ld",&n,&k);
    double num = (double)n/k;
    if(n%k==0 && n>k) //if n is divisible by k
    {
        if(n%2==0 && k%2==0) //n even, k even
            {printf("%ld",((n/k)*(n/k)*(n/k))*2);}
        else//n even, k odd | n odd, k odd |
            {printf("%ld",(n/k)*(n/k)*(n/k));}
    }
    else //if n is not divisible by k
    {
        if(n%2==0 && k%2==0)//n even, k even
        {   
            if(n>k)
                if(num>0.5)
                {printf("%ld", ((n/k)*(n/k)*(n/k))+(((n/k)+1)*((n/k)+1)*((n/k)+1)));}
                else
                {printf("%ld",((n/k))*((n/k))*((n/k))*2);}
            else
            {
                if(num>=0.5)
                    printf("%ld",1);
                else
                    printf("%ld",0);
            }
        }
        else if(n%2!=0 && k%2==0)//n odd, k even
        {
            if(n>k)
            {
                num=num-(int)num;
                if(num>0.5)
                {printf("%ld", ((n/k)*(n/k)*(n/k))+(((n/k)+1)*((n/k)+1)*((n/k)+1)));}
                else
                {printf("%ld",((n/k))*((n/k))*((n/k))*2);}
            }
            else
            {
                if(num>=0.5)
                    printf("%ld",1);
                else
                    printf("%ld",0);
            }
        }
        else// n even, k odd | n odd, k odd |
            {printf("%ld",(n/k)*(n/k)*(n/k));}
    }
    return 0;
}