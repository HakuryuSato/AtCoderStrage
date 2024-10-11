import sys


# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

import math

N, M = map(int, input().split())
MOD = 10**9 + 7

if abs(N - M) > 1:
    print(0)
else:
    ways = (math.factorial(N) * math.factorial(M)) % MOD
    
    if N == M:
        ways = (ways * 2) % MOD
    
    print(ways)



'''
実行時間制限: 2 sec / メモリ制限: 256 MB
n,m=1~10^5

n,mはそれぞれ異なる種類の駒
同じ種類の駒どうしが隣接しないように並べる
並べ方の組み合わせ数を10^9+7で割ったあまりを求めよ

[私の考え]
標準ライブラリを使用して組み合わせを生成する、
組み合わせ数が膨大になるので、可能ならば細かい範囲で割ったあまりとしてカウントしていく

[メモ]
より具体的な説明が必要

'''