import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, T, A = map(int, input().split())
nokori = N - (T + A)

if abs(T - A) > nokori:
    print("Yes")
else:
    print("No")