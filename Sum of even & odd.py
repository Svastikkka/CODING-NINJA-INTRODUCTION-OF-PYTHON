"""
Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
Input format :
Sample Input 1:
1234
Sample Output 1:
6 4


"""
a=input()
b=list(map(int,a))
even=0
odd=0
for i in range(0,len(b)):
    if b[i]%2 ==0:
        even=even+b[i]
    else:
        odd=odd+b[i]
print(even,odd)

