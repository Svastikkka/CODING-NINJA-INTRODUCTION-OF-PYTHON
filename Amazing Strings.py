from collections import Counter

i=input()
j=input()
k=input()



res1 = {x : i.count(x) for x in set(i)}
res2 = {y : j.count(y) for y in set(j)}
res3 = {z : k.count(z) for z in set(k)}



count1 = Counter(res1)
count2 = Counter(res2)
count3 = Counter(res3)

print(count1,count2)
print(count1+count2)
print(count3)

if count3 == count2+count1:
    print("YES")
else:print("NO")



