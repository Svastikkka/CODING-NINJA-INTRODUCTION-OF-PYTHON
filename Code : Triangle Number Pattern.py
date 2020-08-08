"""
6
1
21
321
4321
54321
654321
"""
num=int(input())
for i in range(1,num+1):
    x=[]
    for j in range(1,i+1):
        x.append(str(j))
    print(int("".join(x[::-1])))


#Using While loop
currentRow=1
while currentRow<=num:
    currentCol=currentRow
    while currentCol>=1:
        print(currentCol,end="")
        currentCol=currentCol-1
    currentRow=currentRow+1
    print()