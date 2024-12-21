import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

A, B, C = map(int, input().split())

if A==B+C or A+B==C or B==A+C or A==B==C:
    print('Yes')
else:
    print('No')