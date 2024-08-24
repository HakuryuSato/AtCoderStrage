import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N,K = map(int,input().split())
A = list(map(int,input().split()))

extract = A[-K:]
remain = A[:-K]
result = extract+remain

print(*result)