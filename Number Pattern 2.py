
"""
4
1234
123
12
1
"""
num = int(input())
for i in range(0,num):
    for j in range(1,num+1-i):
        print(j,end="")
    print()
