import sys
from collections import defaultdict

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


Scnt = defaultdict(int)
Tcnt = defaultdict(int)

S = input().strip()
T = input().strip()

for s_char in S:
    Scnt[s_char] += 1
for t_char in T:
    Tcnt[t_char] += 1


for c in "atcoder":
    M = max(Scnt[c], Tcnt[c])
    if Scnt['@'] < M - Scnt[c] or Tcnt['@'] < M - Tcnt[c]:
        print("No")
        exit()
    Scnt['@'] -= M - Scnt[c]
    Scnt[c] = M
    Tcnt['@'] -= M - Tcnt[c]
    Tcnt[c] = M

print("Yes" if Scnt == Tcnt else "No")



'''
[問題文]
実行時間制限: 2 sec / メモリ制限: 1024 MB
S,T=英小文字と'@'からなる 1~2*10^5の文字列（長さは等しい）

@を[a, t, c, o, d, e, r]のいずれかのカードと置き換えて、
一致させることができるならばYesを、そうでないならばNoを出力

入力例1
ch@ku@ai
choku@@i

出力例1
Yes

入力例2
ch@kud@i
akidu@ho

出力例2
Yes

入力例3
aoki
@ok@

出力例3
No


[私の考え]
1.SとTをdict型にして文字数を数える
2.足りない文字が@の変換可能リストに含まれるならば変換
3.一致するかどうか？

'''


