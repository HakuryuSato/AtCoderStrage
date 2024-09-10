import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N,A,B=map(int,input().split())
C = list(map(int,input().split()))

print(C.index(A+B)+1)

