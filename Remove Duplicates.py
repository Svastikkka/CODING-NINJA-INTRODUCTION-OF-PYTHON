"""
xxxyyyzwwzzz
xyzwz
"""
s= [x for x in input()]
n=len(s)
j=0
res=""
for i in range(1,n):
    if s[i] == s[j]:
        s[j] = " "
        j=j+1
    else:
        j=j+1
print(res.join(s).replace(" ",""))