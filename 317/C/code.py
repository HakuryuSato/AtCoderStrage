import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__

N, M = map(int, input().split())
E = [[0]*(N+1)for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  E[a][b] = c #無向グラフなので双方向分格納
  E[b][a] = c


ans = 0
used = [False] * (N + 1) # 訪問済みノード


def dfs(v, s): # DFSを行う再帰関数 v:訪問済み s:経路長
    global ans # グローバル変数を呼び出す
    used[v] = True # vがノード番号となる
    if s > ans: ans=s # 経路長が最大ならば、グローバル関数としてansに格納する
    for i in range(1,N+1):
        #　ノードが訪問済みでなく、経路が存在するなら
        if not used[i] and E[v][i]: # もしE[v][i]が存在しなければ0となる、andで数値を評価すると0はfalse
            dfs(i,s+E[v][i]) # 再帰呼び出し、これによりノードiから見訪問ノード
    used[v]=False #基底ケースとなる、used[v]が狭まっていくため、いつかは処理が完了する。

for i in range(1,N+1): # 全ての開始点から探索する
  dfs(i,0) # どこかの開始点から、経路長0から探索を開始する、
print(ans)