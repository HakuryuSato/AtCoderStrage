import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索？
# %で場所調整
# 全探索は無理 2*10^5 * 2*10^5 4*10^10

# Aの値全てがM以下なら0確定

# 全ての経路の歩数を予め全探索？ 2*10^5

# 組の数を出せばよい

