import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, M, P = map(int, input().split())

count = 0

if N // M > 1:
    N = N - M
    count += 1

count = count + (N//P)

print(count)