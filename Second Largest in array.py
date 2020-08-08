num=int(input())
n=list(map(int,input().split()))
if num<=1:
    print(-2147483648)
else:
    n=sorted(set(n))
    print(n[-2])