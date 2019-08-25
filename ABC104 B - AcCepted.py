#ABC104 B - AcCepted
#文字列.replace(置換前の文字列, 置換後の文字列, 最大回数)
s=input()
if s[0]=="A" and "C" in s[2:-1] and s[1:].replace("C","",1).islower():
    print("AC")
else:
    print("WA")
