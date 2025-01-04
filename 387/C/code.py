import sys
sys.setrecursionlimit(10**7)

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

L,R=map(int,input().split())
