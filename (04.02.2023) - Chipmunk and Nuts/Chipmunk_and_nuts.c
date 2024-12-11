int main()
{   
    int n,i,result=0;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
        if(arr[i]>=10)
        {result+=(arr[i]-10);}
        else
        {result+=0;}
    }
    printf("%d",result);
    return 0;
}