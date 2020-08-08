"""
hra   = 20% of basic
da    = 50% of basic
allow = 1700 if grade = ‘A’
allow = 1500 if grade = ‘B’
allow = 1300 if grade = ‘C' or any other character
pf    = 11% of basic.

    totalSalary = basic + hra + da + allow – pf

"""

num,g=input().split()
hra=(20*int(num)/100)
da=(50*int(num)/100)
allow=0
if g == "B":
    allow=allow+1500
elif g == "A":
    allow=allow+1700
else:
    allow = allow + 1300


pf=(11*int(num)/100)
salary = int(num)+hra+da+allow-pf
print(round(salary))