import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int,input().split()))

A.sort()

for i in range(len(A) - 1):
    if A[i + 1] != A[i] + 1:
        print(A[i] + 1)
        break