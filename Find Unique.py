j=int(input())
num=list(map(int,input().split()))
res=0
count=10000000
for i in range(0,j):
    if num.count(num[i])<count:
        count=num.count(num[i])
        res=num[i]
print(res)