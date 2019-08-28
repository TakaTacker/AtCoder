#ABC001 A - センター採点
n=input()
c=list(input())
print(max(c.count("1"),c.count("2"),c.count("3"),c.count("4")),
     min(c.count("1"),c.count("2"),c.count("3"),c.count("4")))
