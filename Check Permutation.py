s1=input()
s2=input()
if len(s1) == len(s2):
    s11=sorted(s1)
    s22=sorted(s2)
    for i in  range(len(s11)):
        if s11[i] == s22[i]:
            pass
        else:
            print("false")
            break
    else:print("true")