import sys
from itertools import permutations

# ローカル用
# file_number = 5
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


# 1 <= i < j <=Nを満たす整数の組i,jを一つ選び、A[i][j]円を支払って、頂点iと頂点jを結ぶ辺なければ追加、あれば除去
# ijは異なる、i<jとなる
# GとHを同型にするには、少なくとも何円支払う必要があるか？


N = int(input())
Mg = int(input())
edges_G = [tuple(map(int, input().split())) for _ in range(Mg)]

Mh = int(input())
edges_H = [tuple(map(int, input().split())) for _ in range(Mh)]
A = [list(map(int, input().split())) for _ in range(N - 1)]

set_G = set((min(u, v), max(u, v)) for u, v in edges_G)
set_H = set((min(a, b), max(a, b)) for a, b in edges_H)

min_cost = float('inf')


# 全ての頂点の並べ替えを試す
for perm in permutations(range(1, N + 1)):

    # perm[i-1]がi番目の頂点に対応
    perm_map = {i: perm[i - 1] for i in range(1, N + 1)}
    
    # permに基づいてGの辺を変換
    transformed_G = set((min(perm_map[u], perm_map[v]), max(perm_map[u], perm_map[v])) for u, v in set_G)
    
    # コストの計算
    cost = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if ((i, j) in transformed_G) != ((i, j) in set_H):
                cost += A[i - 1][j - i - 1]
    
    # 最小コストの更新
    min_cost = min(min_cost, cost)

# 結果の出力
print(min_cost)
