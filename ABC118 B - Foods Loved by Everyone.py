#ABC118 B - Foods Loved by Everyone
n,m=map(int,input().split(" ")) 
S=set(range(1,m+1)) #1からmまでの数値でsetを生成
for i in range(n):　#n回繰り返し
    K, *A = map(int, input().split(" "))　#K個の要素をもつリストAiを生成。引数*Aで、inputしたAをタプルで渡す
    S &=set(A) #S = S and set(A):論理積。共通した要素のみを抽出していく
print(len(S))
