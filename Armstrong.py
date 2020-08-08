num=input()
n=[int(i) for i in num]
count=0
for j in range(len(n)):
    count=count+n[j]**len(n)
if count==int(num):
    print("true")
else:print("false")
