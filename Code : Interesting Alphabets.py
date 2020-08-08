"""
5
E
DE
CDE
BCDE
ABCDE

"""
l=['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=int(input())
c=num
for i in range(1,num+1):
    for j in range(0,i):
        print(l[c+j-1],end="")
    c = c - 1
    print()
