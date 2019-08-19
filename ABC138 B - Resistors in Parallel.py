#ABC138 B - Resistors in Parallel
N=int(input())
A=list(map(int,input().split(" ")))
S=0
for i in range(N):
    S=S + 1/A[i]
print(1/S)
