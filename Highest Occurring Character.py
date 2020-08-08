s=list(map(str,input().strip()))
d={}
for i in s:
    if i not in d:
        d.update({i:s.count(i)})
print(max(d,key=d.get))