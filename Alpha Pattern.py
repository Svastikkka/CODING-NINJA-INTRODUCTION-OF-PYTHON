"""
3
 A
 BB
 CCC

"""
l=['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=int(input())
c=0
for i in range(1,num+1):
    for j in range(0,i):
        print(l[i-1],end="")
    print()
    c=c+1