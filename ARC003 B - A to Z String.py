#ARC003 B - A to Z String
s=input()
left,right=0,0
left = s.index("A")
right = s[::-1].index("Z")
print(len(s)- right-left)
