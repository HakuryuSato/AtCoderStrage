import sys
from itertools import product

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

n = int(input())
for x, y, z in product(range(n + 1), repeat=3):
    if x + y + z <= n:
        print(x, y, z)
