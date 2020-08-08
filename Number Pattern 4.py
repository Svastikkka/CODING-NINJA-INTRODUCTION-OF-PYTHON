"""
7
1
11
111
1111
11111
111111
1111111

"""

num = int(input())
for i in range(1,num+1):
    for j in range(0,i):
        print(1,end="")
    print()