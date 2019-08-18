#ABC136 C - Build Stairs
N=int(input())
H=list(map(int, input().split(" ")))
A = H[0]
ans = "Yes"
for i in range(1,N):
    if A < H[i]:
        A = H[i]
    elif A - H[i] > 1:
        ans = "No"
        break
print(ans)
