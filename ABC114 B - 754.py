#ABC114 B - 754
S=input()
ans=999999999
for i in range(len(S) - 2):
    a = int(S[i:i+3])
    ans = min(ans, abs(a-753))
print(ans)
