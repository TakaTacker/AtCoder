#ABC094 B - Toll Gates
#https://atcoder.jp/contests/abc094/tasks/abc094_b

N,M,X=(map(int, input().split(" ")))
S= sum(int(i)<X for i in input().split(" "))
print(min(S, M-S))
