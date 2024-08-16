import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
P = list(map(int, input().split()))

m = 0
for i in range(1, N):
    m = max(m, P[i])

print(max(0, m + 1 - P[0]))
