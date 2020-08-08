j=int(input())
num=list(map(int,input().split()))
count=1
res=0
for i in range(0,j):
    if num.count(num[i])>count:
        res=num[i]

print(res)
