import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__

N = int(input())

A = N * [0]

for i in range(N):
    A[i] = list(map(int, input().split()))


max_len = (max(max(row) for row in A))

field = [[0] * max_len for _ in range(max_len)]

for i in range(N):
    

# for i in range(N):

