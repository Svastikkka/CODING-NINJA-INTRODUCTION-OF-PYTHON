"""

7  Number is always odd
   *
  ***
 *****
*******
 *****
  ***
   *
"""


n=int(input())
firstHalf = (n+1)//2
secondHalf=n//2

currentRow=1
while currentRow<=firstHalf:
    spaces=1
    while spaces<=(firstHalf-currentRow):
        print(" ",end="")
        spaces=spaces+1

    currentCol=1
    while currentCol<=(2*currentRow)-1:
        print("*",end="")
        currentCol=currentCol+1

    print()
    currentRow+=1

