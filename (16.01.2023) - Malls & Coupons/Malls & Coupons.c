#include <stdio.h>
#include <stdlib.h>
int main() {
    long num_of_items, result=0, coupons, reducFactor, temp, i, j;
    scanf("%ld %ld %ld",&num_of_items, &coupons, &reducFactor);
    long cost_array[num_of_items];
    long times,pivot;
    for(i=0;i<num_of_items;i++)
    {
        scanf("%ld",&cost_array[i]);
        //reducing
        while(cost_array[i]>=reducFactor && coupons!=0)
        {
            times=1;
            times=(cost_array[i]-(cost_array[i]%reducFactor))/reducFactor;
            if(coupons>=times) {
                cost_array[i]=cost_array[i]-reducFactor*times;
                coupons=coupons-times;
            } else {
                cost_array[i]=cost_array[i]-reducFactor*coupons;
                coupons=0;
            }
        }
    }
    for(i=0;i<num_of_items;i++)
    {
        //sorting
        pivot = i;
        for (j = i + 1; j < num_of_items; j++) 
        {
            if (cost_array[j] > cost_array[pivot]) 
            {
                pivot = j;
            }
        }
        temp = cost_array[i];
        cost_array[i] = cost_array[pivot];
        cost_array[pivot] = temp;
        //zeroing
        if(cost_array[i]>0)
        {
            if(coupons!=0)
            {
                cost_array[i]=0;
                coupons--;
            }
            else
            {
                break;
            }
        }
        result=result+cost_array[i];
    }
    for(i=i;i<num_of_items;i++)
    {
      result=result+cost_array[i];  
    }
    printf("%ld",result);
    return 0;
}



JAVA TO C:

#include <stdio.h>
#include <stdlib.h>
int main() {
    long n,k,x,count,i,j,temp,result=0,pivot;
    scanf("%ld%ld%ld",&n,&k,&x);
    long cost_array[n];
    for(i=0;i<n;i++)
    {
        scanf("%ld",&cost_array[i]);
    }
    for(i=0;i<n && k!=0;i++)
    {
        if(cost_array[i]/x > k)
        {
            count=k;
        }
        else
        {
            count=(cost_array[i]/x);
        }
        cost_array[i]=cost_array[i]-(count*x);
        k=k-count;
    }
    // for(i=0;i<n;i++) //sorting
    // {
    //     pivot = i;
    //     for (j = i + 1; j < n; j++) 
    //     {
    //         if (cost_array[j] < cost_array[pivot]) 
    //         {
    //             pivot = j;
    //         }
    //     }
    //     temp = cost_array[i];
    //     cost_array[i] = cost_array[pivot];
    //     cost_array[pivot] = temp;
    // }
    for(i=0;i<n-k;i++)
    {
        result=result+cost_array[i];
    }
    printf("%ld",result);
}