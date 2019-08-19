#ABC049 C - 白昼夢 / Daydream
#inputしたもじれつをから、問題設定にある文字列を消去（replace）していく
#"er"がつくものは2番めに書く
s=input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
if s:
    print("NO")
else:
    print("YES")
