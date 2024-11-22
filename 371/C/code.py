import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__


# N個の頂点からなる単純無向グラフG,H
N=int(input()) # 頂点個数 1~8

Mg=int(input()) # グラフGの辺の数 0~28
G=[0]*Mg # グラフG
for i in range(Mg):
    G[i]=list(map(int,input().split()))

Mh=int(input()) # グラフHの辺の数 0~28
H=[0]*Mh # グラフH
for i in range(Mh):
    H[i]=list(map(int,input().split()))

A=[0]*(N-1) # コスト (1~10^6)
for i in range(N-1):
    A[i]=list(map(int,input().split()))


# GとHが異なり続ける限りループ?

# 1 <= i < j <=Nを満たす整数の組i,jを一つ選び、A[i][j]円を支払って、頂点iと頂点jを結ぶ辺なければ追加、あれば除去
# ijは異なる、i<jとなる

# GとHを同型にするには、少なくとも何円支払う必要があるか？


edges_G = set(tuple(sorted(edge)) for edge in G)
edges_H = set(tuple(sorted(edge)) for edge in H)


if len(edges_G)>len(edges_H):
    add_edges = edges_H - edges_G

