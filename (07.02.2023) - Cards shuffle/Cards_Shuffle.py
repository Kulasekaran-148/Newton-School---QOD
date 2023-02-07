Problem Statement
We have 4 cards with an integer 1 written on it, 4 cards with 2, …, 4 cards with N, for a total of 4N cards.
Alexa shuffled these cards, removed one of them, and gave you a pile of the remaining 4N−1 cards. The i- th card (1≤i≤4N−1) of the pile has an integer Ai written on it.

Find the integer written on the card removed by Alexa.
Input
The first line of input contains an integer N.
The second line contains N space separated integers as follows:

N
A1 A2. . AN

Constraints
1≤N≤10^5
1≤Ai≤N(1≤i≤4N−1)
For each k(1≤k≤N), there are at most 4 indices i such that Ai=k.
All values in input are integers.
Output
Print the answer.
Example
Sample Input 1
3
1 3 2 3 3 2 2 1 1 1 2
Sample Output 1
3

Sample Input 2
1
1 1 1
Sample Output 2
1

Sample Input 3
4
3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
Sample Output 3
2

n=int(input())
input_string=input()
cards=input_string.split()
cards=[int(i) for i in cards]
hashtable=[0 for i in range(n)]
for i in range(4*n-1):
    hashtable[cards[i]-1]+=1
print(hashtable.index(3)+1,end="")