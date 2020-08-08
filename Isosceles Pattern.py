""""
7
       1
      121
     12321
    1234321
   123454321
  12345654321
 1234567654321
"""

num=int(input())
i=1
while i <= num:
    j=1
    while j <= num-i+1:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print(k,end="")
        k=k+1
    l= i-1
    while l>=1:
        print(l,end="")
        l=l-1
    i=i+1
    print()