import sys
from collections import deque

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

H, W, D = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# 初期化
result = 0
queue = deque()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 初期状態設定
for h in range(H):
    for w in range(W):
        if grid[h][w] == "H":
            result += 1
            queue.append((h, w))
            grid[h][w] = 0

# 幅優先探索
while queue:
    h, w = queue.popleft()
    if grid[h][w] == D:
        continue
    for dh, dw in directions:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and grid[nh][nw] == ".":
            grid[nh][nw] = grid[h][w] + 1
            result += 1
            queue.append((nh, nw))

# 結果を出力
print(result)
