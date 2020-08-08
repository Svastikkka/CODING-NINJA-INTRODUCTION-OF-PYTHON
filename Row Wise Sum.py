"""
4 2

1 2
3 4
5 6
7 8

3 7 11 15


2 5
4 5 3 2 6
7 5 3 8 9


20 32
"""

x,y=list(map(int,input().split()))
num=list(map(int, input().split()))
res=[[num[(i*y)+j] for j in range(y)] for i in range(x)]
print(res)



