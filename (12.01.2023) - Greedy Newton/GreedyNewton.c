#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    long long ncookies, ecookies, count, i;
    scanf("%lld%lld%lld",&ncookies, &ecookies, &count);
    if(count<ncookies)
    {
        ncookies=ncookies-count;
    }
    else
    {
        count=count-ncookies;
        ncookies=0;
        if(count<ecookies){
            ecookies=ecookies-count;
        }
        else{
            ecookies=0;
        }
        
    }
    printf("%lld %lld",ncookies,ecookies);
    return 0;
}