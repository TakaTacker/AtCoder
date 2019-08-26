#ABC113 B - Palace
n=int(input())
T, A = map(int,input().split())
H=list(map(int,input().split()))
ans=A-(T - H[0]* 0.006)
place=1
for i in range(1,n):
    if abs(ans)>abs(A-(T - H[i]* 0.006)):
        ans=A-(T - H[i]* 0.006)
        place=i+1
print(place)
