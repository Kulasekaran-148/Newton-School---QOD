Problem Statement
Bob loves to play with numbers. He has an integer N. Find the number of digits that N has in base K.
Input
The input contains two space-separated integers in the following format:
N K

Constraints
All values in the input are integers.
1 ≤ N ≤ 109
2 ≤ K ≤ 10
Output
Print the number of digits that N has in base K.
Example
Sample Input 1
11 2
Sample Output 1
4

Sample Input 2
1010101 10
Sample Output 2
7

Sample Input 3
314159265 3
Sample Output 3
18

n,k=map(int,input().split())
def dec_to_base(num,base): 
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10) 
        num //= base
    base_num = base_num[::-1] 
    return base_num
converted_num = str(dec_to_base(n,k))
print(len(converted_num),end="")