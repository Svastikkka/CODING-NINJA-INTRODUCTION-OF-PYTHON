num=int(input())
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
if flag:
    print("Not a Prime")
else:print("Prime")