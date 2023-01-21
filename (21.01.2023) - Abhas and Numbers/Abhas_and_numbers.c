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

Alternate code:

#include <stdio.h>
#include <math.h>
long power(long value, long exponent)
{
    int i;
    long result=1;
    for(i=1;i<=exponent;i++)
    {result*=value;}
    return result;
}
int main() {
    long n,k;
    scanf("%ld %ld",&n,&k);
    long num_int=(int)n/k;
    double num_float = (double)n/k;
    if(n<k)
    {
        if(n%2==0 || k%2==0)
        {
        if(num_float>=0.5)
            { printf("%d",1); }
        else
            { printf("%d",0); }
        }
        else
        {printf("%d",0);}
    }
    else if(n%k==0) //Divisible
    {
        if(n%2==0 && k%2==0) //Both n & k are even. ans is ((num_int)^3)*2
        { printf("%ld",(power((num_int),3))*2); }
        else //n is even, k is odd (or) both n and k are odd, ans is (num_int)^3
            { printf("%ld",power((num_int),3)); }
    }
    else //Non-Divisible
    {
        if((n%2!=0 && k%2==0) || (n%2==0 && k%2==0))//n is odd & k is even (or) Both n & k are even 
        {
            if((num_float-(int)num_float)<0.5) //if decimal part of n/k is less than 50%, ans is ((num_int)^3)*2
                { printf("%ld",(power((num_int),3))*2); }
            else //if decimal part of n/k is more than 50%, ans is (num_int)^3 + (num_int +1)^3
                { printf("%ld", power((num_int),3)+power((num_int+1),3)); }
        }
        else //n is even, k is odd (or) both n and k are odd, ans is (num_int)^3
            { printf("%ld",power((num_int),3)); }
    }
    return 0;
}