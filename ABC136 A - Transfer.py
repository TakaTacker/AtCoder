#ABC136 A - Transfer
a,b,c=map(int,input().split())
if a-b>=c:
    print(0)
elif a-b<c:
    print(abs(c-a+b))
