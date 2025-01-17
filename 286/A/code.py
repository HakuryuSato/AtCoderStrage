import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N, P, Q, R, S = map(int, input().split())

A = list(map(int, input().split()))
A[P - 1 : Q], A[R - 1 : S] = A[R - 1 : S], A[P - 1 : Q]

print(*A)
