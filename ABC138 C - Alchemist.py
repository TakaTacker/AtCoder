#ABC138 C - Alchemist
N=int(input())
v=sorted(list(map(int,input().split(" "))))
s=v[0]
for i in range(1,N):
    s = (s+v[i])/2
print(s)
