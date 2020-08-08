
"""
5
        1
      23
    345
  4567
56789

"""
num=int(input())
count=num
for i in range(1,num+1):
    while count>1:
        print("  ",end="")
        count=count-1
    for j in range(0,i):
        print(i+j,end="")
    print()
    count=num-i