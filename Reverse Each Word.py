s=list(map(str,input().split()))
s1=[]
for i in range(len(s)):
    s1.append(s[i][::-1])

print(" ".join(s1))