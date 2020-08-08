"""
Given a number N, print sum of all even numbers from 1 to N.

"""
n=int(input())
sum=0
for i in range(1,n+1):
    if (sum+i)%2==0:
        sum=sum+i
print(sum)