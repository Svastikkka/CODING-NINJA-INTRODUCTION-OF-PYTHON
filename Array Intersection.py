num1=int(input())
n1=list(map(str,input().split()))
num2=int(input())
n2=list(map(str,input().split()))

res=[]
if len(n1)>len(n2):
    for i in range(0,len(n1)):
        if n1[i] in n2:
            res.append(n1[i])
            n2.remove(n1[i])

else:
    for i in range(0,len(n2)):
        if n2[i] in n1:
            res.append(n2[i])
            n1.remove(n2[i])
for i in range(0, len(res)):
        print(int(res[i]))