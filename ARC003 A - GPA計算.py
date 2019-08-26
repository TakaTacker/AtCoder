#ARC003 A - GPA計算
n=int(input())
r=input()
s=0
for i in r:
    s=s + ("FDCBA".index(i))
print(s/n)
