while True:
    o=int(input())
    if o==1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif o==2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif o==3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif o==4:
        a = int(input())
        b = int(input())
        print(a//b)
    elif o==5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif o>6:
        print("Invalid Operation")
    elif o==6:
        break


