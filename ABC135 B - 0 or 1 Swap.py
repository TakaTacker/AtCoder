#ABC135 B - 0 or 1 Swap
n=int(input())
a=[i for i in range(1,n+1)]
p=list(map(int,input().split()))
cnt=0
for j in range(n):
    if a[j]!=p[j]:
        cnt+=1
print("YES" if cnt==2 or cnt==0 else "NO")
