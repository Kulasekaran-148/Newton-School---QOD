Problem Statement
There are 4 squares lined up horizontally. You are given a string S of length 4 consisting of 0 and 1.
If the ith character of S is 1, there is a person in the ith square from the left; if the ith character of
S is 0, there is no person in the ith square from the left.
Now, everyone will move to the next square to the right simultaneously. With this move, the person who was originally in the rightmost square will disappear. Determine if there will be a person in each square after the move. Print the result as a string in the same format as S. (See also Sample Input/Output for clarity.)
Input
The input consists of a single string.

Constraints
S is a string of length 4 consisting of 0 and 1.
Output
Print a string of length 4 such that the i- th character is 1 if there will be a person in the i- th square from the left after the move, and 0 otherwise.
Example
Sample Input 1
1011
Sample Output 1
0101

Sample Input 2
0000
Sample Output 2
0000

Sample Input 3
1111
Sample Output 3
0111

a = input()
b = [0,a[0],a[1],a[2]]
for i in range(4):
    print(str(b[i]),end="")