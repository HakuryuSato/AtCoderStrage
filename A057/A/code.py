

# コメントアウトすること -------------------------------------------------
# ローカル用
file_number = 2
sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
# sys.stdin = sys.__stdin__
# 上記コメントアウトすること　 -------------------------------------------------

import sys
from itertools import product

n = int(input())
G = [list(map(int, input())) for _ in range(n)]

directions = list(product([-1, 0, 1], repeat=2))
directions.remove((0, 0))

ans = 1

for i in range(n):
    for j in range(n):
        for dx, dy in directions:
            for sign in (1, -1):
                length = 1
                x, y = i, j
                while True:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < n):
                        break
                    if G[nx][ny] == G[x][y] + sign:
                        length += 1
                        x, y = nx, ny
                    else:
                        break
                ans = max(ans, length)
print(ans)

