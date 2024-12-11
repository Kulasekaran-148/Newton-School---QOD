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