import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n= int(input())

def rec (n):
    if n == 0:
        return 1
    else:
        return n * rec(n-1)

print(rec(n))