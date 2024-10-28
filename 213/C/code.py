import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

h,w,n = map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(n)]

l