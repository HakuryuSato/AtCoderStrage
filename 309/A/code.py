import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

A, B = map(int, input().split())

if (A % 3 != 0 and A + 1 == B):
    print("Yes")
else:
    print("No")
