import sys


# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

from collections import defaultdict

n = int(input())
mp = defaultdict(int)

A = list(map(int, input().split()))

for a in A:
    mp[a] += 1

for a in sorted(mp.keys(), reverse=True):
    print(mp[a])

for _ in range(n - len(mp)):
    print(0)


'''
実行時間2秒 メモリ1GB
[問題文]
Aに含まれる整数のうち、Aiより大きいものはちょうどK種類
N=1~2*10^5
Ai=1~10^9

入力例
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527

出力例
2
1
2
1
2
1
1
0
0
0


[私の考え]
大きい順にソートして、数Aiより大きいものの個数を予め求める(種類であることに注意)
AでループしてAiのインデックスから、個数を順次出力


'''