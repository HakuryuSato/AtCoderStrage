import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__

N = int(input())
A = []
for i in range(N):
    A.append([int(char) for char in input().strip()])

result = N * [[0] * N]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            result[i][j] = A[i + 1][j]
        elif i == N - 2 and j == 0:
            result[i][j] = A[i + 1][j]
        elif i == 1 and j == N - 1:
            result[i][j] = A[i + 1][j]
        elif i == 0:
            result[i][j] = A[i + 1][j]
        else:
            result[i][j] = A[i][j]

print([row for row in result])
