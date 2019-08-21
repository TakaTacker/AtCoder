#ABC070 B - Two Switches
a,b,c,d = map(int,input().split())
if b<=c or d<=a:
    print(0)
elif a<=c<=d<=b:
    print(d-c)
elif a<=c<=b<=d:
    print(b-c)
elif c<=a<=b<=d:
    print(b-a)
elif c<=a<=d<=b:
    print(d-a)
