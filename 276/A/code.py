import sys

# ローカル用
# file_number = 2

# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n=input().rfind('a')

if n == -1:
    print(-1)
else:
    print(n+1)
