import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N, R = map(int, input().split())

for _ in range(N):
    d, a = map(int, input().split())

    if (d == 1 and R >= 1600 and R <= 2799) or (d == 2 and R >= 1200 and R <= 2399):
        R += a


print(R)