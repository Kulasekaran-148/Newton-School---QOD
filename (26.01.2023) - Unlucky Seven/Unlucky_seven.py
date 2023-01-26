Mahi hates the number 7.

We are interested in integers without the digit 7 in both decimal and octal. How many such integers are there between 1 and N (inclusive)?
Input
Input is given from Standard Input in the following format:
N

Constraints
1≤N≤10^5

N is an integer.
Output
Print an integer representing the answer.
Example
Sample Input 1
20
Sample Output 1
17
Sample Input 2
100000
Sample Output 2
30555

n = int(input())
count=0
for i in range(1,n):
    digitoct=str(oct(i))
    digit=str(i)
    if "7" in digitoct or "7" in digit:
        count=count+1
print(int(n-count-1), end="")