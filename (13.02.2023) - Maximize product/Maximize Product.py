Problem Statement
Given are integers a, b, c, and d. If x and y are integers and a≤x≤b and c≤y≤d hold, what is the maximum possible value of x*y?
Input
The input consists of four space-separated integers.
a b c d

Constraints
−10^9≤a≤b≤10^9
−10^9≤c≤d≤10^9

All values in the input are integers.
Output
Print the maximum product.
Example
Sample Input 1
1 2 1 1
Sample Output 1
2

Sample Input 2
3 5 -4 -2
Sample Output 2
-6

Sample Input 3
-1000000000 0 -1000000000 0
Sample Output 3
1000000000000000000

a,b,c,d = map(int, input().split())
result=max(a*c,a*d,b*c,b*d)
print(result,end="")