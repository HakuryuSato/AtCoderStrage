import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = max(A)
max_B = max(B)

print(max_A + max_B)
