num=int(input())
s=[char for char in input()]
l=[]

for i in range(0,num):
    if l.count(s[i].lower()) == 1:
        pass #you can use continue here to
    else:l.append(s[i].lower())

if len(l)==26:
    print("YES")
else:print("NO")


