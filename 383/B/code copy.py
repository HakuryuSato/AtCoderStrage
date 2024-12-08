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

# ユカセルのみ
floor_cells = [(i, j) for i in range(H) for j in range(W) if S[i][j] == "."]


humidified_dict = {}
# 事前に全ての組み合わせを計算
for x, y in floor_cells:
    humidified_dict[x, y] = {
         (i, j) for i,j in floor_cells if abs(x - i) + abs(y - j) <= D
    }

total_humidified = 0

# 床セルから二つ選び、辞書のキーから値の合計を計算
for (x1, y1), (x2, y2) in combinations(floor_cells, 2):
    total_humidified = max(
        total_humidified, (len(humidified_dict[(x1, y1)] | humidified_dict[(x2, y2)]))
    )

print(total_humidified)
