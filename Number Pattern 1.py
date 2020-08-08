"""
4
1
11
202
3003

"""
num=int(input())
for i in range(1,num+1):
    for j in range(0,i):
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(x,end="")
            else:print(0,end="")
    print("")