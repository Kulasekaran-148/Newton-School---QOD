Problem Statement
Emilia is playing with bitwise xor. She is given integers A and B between 0 and 255 (inclusive).
Help her find a non-negative integer C such that A xor C = B => (A⊕C = B).
It can be proved that there uniquely exists such C, and it will be between 0 and 255 (inclusive).
Input
The input consists of two space separated integers A and B.

Constraints
0 ≤ A, B ≤ 255
All values in input are integers.
Output
Print the answer.
Example
Sample Input 1
3 6
Sample Output 1
5

Sample Input 2
10 12
Sample Output 2
6

a,b = map(int, input().split())
print(a^b, end="")