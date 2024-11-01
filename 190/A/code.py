import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


A, B, C = map(int, input().split())
if A + C > B:
    print("Takahashi")
else:
    print("Aoki")
