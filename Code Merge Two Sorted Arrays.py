num1=int(input())
n1=list(map(int,input().split()))
num2=int(input())
n2=list(map(int,input().split()))

n3=[]
for i in range(len(n1)):
    n3.append(n1[i])
for i in range(len(n2)):
    n3.append(n2[i])
n3=sorted(n3)
for i in range(len(n3)):
    print ("%d " %n3[i],end="")