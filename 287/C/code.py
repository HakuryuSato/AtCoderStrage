import sys
sys.setrecursionlimit(10**7)

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

# パスグラフか判定
n, m = map(int, input().split())

G = [list() for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


if n != m + 1:
    exit(print("No"))


for g in G:
    if len(g) > 2:
        exit(print("No"))


visited = [1] + [0] * (n)

def dfs(i):
    if visited[i] == 0:
        visited[i] = 1
        for next in G[i]:
            dfs(next)

dfs(1)
if sum(visited) != n + 1:
    exit(print("No"))


print("Yes")
