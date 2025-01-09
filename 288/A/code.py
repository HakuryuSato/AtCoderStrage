import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n=int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(a+b)
