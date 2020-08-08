import itertools

s=list(map(str,input().strip()))
s1=""
for i in itertools.groupby(s):
    s1=s1+str(i[0])
print(s1)    