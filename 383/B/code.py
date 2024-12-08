import sys
from itertools import combinations

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
# sys.stdin = sys.__stdin__

# 入力
H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]
floor_cells = [(i, j) for i in range(H) for j in range(W) if S[i][j] == '.']

# 各床セルをキーとした加湿可能範囲を辞書に事前計算
humidified_dict = {}
for x, y in floor_cells:
    humidified_dict[(x, y)] = {(i, j) for i, j in floor_cells if abs(x - i) + abs(y - j) <= D}

# 最大加湿範囲を計算
max_humidified = 0
for (x1, y1), (x2, y2) in combinations(floor_cells, 2):
    total_humidified = humidified_dict[(x1, y1)] | humidified_dict[(x2, y2)]
    max_humidified = max(max_humidified, len(total_humidified))

print(max_humidified)

