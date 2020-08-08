"""
7
      1
     212
    32123
   4321234
  543212345
 65432123456
7654321234567

spaces=0 to num-i
increasing= i to 2*i-1
decresing = 2*i-2 to i-1

"""
num=int(input())
i=1
while num>=i:
    spaces=1
    while spaces<=(num-i):
        print(" ",end="")
        spaces=spaces+1
    k=i
    while k>=1:
        print(k,end="")
        k=k-1
    j=2
    while j<=i:
        print(j,end="")
        j=j+1

    print()
    i += 1
