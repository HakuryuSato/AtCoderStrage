import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


N,M=map(int,input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

M_plus = M + 2
max_Li = [0] * M_plus

for Li, Ri in intervals:
    max_Li[Ri] = max(max_Li[Ri], Li)

for r in range(1, M + 1):
    max_Li[r] = max(max_Li[r], max_Li[r - 1])

S = 0
for r in range(1, M + 1):
    S += min(max_Li[r], r)

T = M * (M + 1) // 2
print(T - S)












'''
[問題文]
実行時間2秒 メモリ1GB制限

正整数列intervalsと整数Mが与えられます。
1<=l<=r<=M及び、全ての1<=i<=Nに対し、区間l,rはく勘Li,Riを完全には含まない。
という条件を満たす整数の組(l,r)の個数を求めてください

NM=1~2*10^5
Li,RI=1~2*10^5

入力例
6 20
8 12
14 20
11 13
5 19
4 11
1 6

出力例
102

[私の考え]
・区間に含むかどうかは、標準ライブラリで列挙？
・intervals [i][0]と、intervals [i][1]が同じならば、その区間は存在しない(例1,1や2,2など。)
・全ての区間に対して適用されるので、最も小さい区間から探索したほうが良いか？

'''
