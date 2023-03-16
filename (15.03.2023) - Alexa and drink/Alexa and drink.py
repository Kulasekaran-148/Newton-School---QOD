Problem Statement
Alexa has a drink that has A kilocalories of energy per 100 milliliters. How many kilocalories of energy does B milliliters of this drink have?
Input
The input consists of two space separated integers A and B.

Constraints
0 ≤ A, B ≤1000
All values in input are integers.
Output
Print a number representing the answer up to 2 decimal places.
Your output is considered correct when its absolute or relative error from our answer is at most 10−2.
Example
Sample Input 1
45 200
Sample Output 1
90.00

Sample Input 2
37 450
Sample Output 2
166.50

Sample Input 3
50 0
Sample Output 3
0.00

a,b = map(int,input().split())
print("%0.2f"%((b/100)*a),end="")