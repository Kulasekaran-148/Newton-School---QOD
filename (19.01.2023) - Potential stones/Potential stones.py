Problem Statement
There are 2000001 stones placed on a number line. The coordinates of these stones are −1000000, −999999, −999998, …, 999999, 1000000. Among them, some K consecutive stones are painted black, and others are painted white. Additionally, we know that the stone at coordinate X is painted black.
Print all coordinates that potentially contain a stone painted black, in ascending order.
Input
The input consists of two space-separated integers.
K X

Constraints
1≤K≤100
0≤X≤100
All values in the input are integers.
Output
Print all coordinates that potentially contain a stone painted black, in ascending order, with spaces in between.
Example
Sample Input 1
3 7
Sample Output 1
5 6 7 8 9

Sample Input 2
4 0
Sample Output 2
-3 -2 -1 0 1 2 3

Sample Input 3
1 100
Sample Output 3
100

k,x = map(int, input().split())
for i in range(x-k+1,x+k):
    print(i,end=" ")