
"""
7
*
 **
  ***
   ****
  ***
 **
*


"""
num = int(input())
for i in range(1,num+1):
    if i <= round(num/2):
        for j in range(1,i):
            print(" ",end="")
        for j in range(0,i):
            print("*",end="")
    else:
        for j in range(1,num-i+1):
            print(" ",end="")
        for j in range(0,num-i+1):
            print("*",end="")
    print()