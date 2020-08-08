"""
4
   *
  ***
 *****
*******

"""
num=int(input())
i=1

while i<=num:
    j = 0
    while j<num-i:
        print(" ",end="")
        j=j+1
    k=0
    while k<i:
        print("*",end="")
        k=k+1
    k=1
    while k<i:
        print("*",end="")
        k=k+1
    i=i+1
    print()

