"""
Pattern for N = 4
4444
333
22
1

"""

num=int(input())
i=1
while i<=num:
    j=1
    while j<=num-i+1:
        print(num,end="")
        j=j+1
    num=num-1
    print()





