import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

a,b = map(int,input().split())

print('Yes' if b//a == 2 else 'No')