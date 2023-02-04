Problem Statement
There are N trees. The ith tree bears Ai nuts. Chipmunk will harvest nuts from the trees in the following manner:
From a tree with 10 or fewer nuts, she does not take nuts.
From a tree with more than 10 nuts, she takes all but 10 nuts.
Find the total number of nuts Chipmunk will take from the trees.
Input
Input is given from Standard Input in the following format:
N
A1… AN
​
Constraints
1 ≤ N ≤ 1000
0 ≤ Ai ≤ 1000
All values in the input are integers.
Output
Print the answer.
Example
Sample Input 1
3
6 17 28
Sample Output 1
25

Sample Input 2
4
8 9 10 11
Sample Output 2
1

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