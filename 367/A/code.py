import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

A, B, C = map(int, input().split())

if B < C:
    if B <= A < C:
        print("No")
    else:
        print("Yes")
else:
    if A >= B or A < C:
        print("No")
    else:
        print("Yes")