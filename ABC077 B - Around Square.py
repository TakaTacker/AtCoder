#ABC077 B - Around Square
N=int(input())
for i in range(1,N+1):
    if i*i>N:
        s=(i-1)**2
        break
if N==1:
    print(N)
else:
    print(s)
