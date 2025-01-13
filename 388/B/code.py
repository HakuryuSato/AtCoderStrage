import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N, D = map(int, input().split())
T_L = [tuple(map(int, input().split())) for _ in range(N)]


for k in range(1, D + 1):
    max_weight = 0
    for T, L in T_L:
        weight = T * (L + k)
        max_weight = max(weight, max_weight)
    print(max_weight)
