import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int, input().split()))

result = [a for a in A if a % 2 == 0]

print(*result)
