import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
A=list(map(int,input().split()))

if len(A) < 2:
    print('No')
else:
    is_geometric = True
    for i in range(1, len(A) - 1):
        if A[i] ** 2 != A[i - 1] * A[i + 1]:
            is_geometric = False
            break
    print('Yes' if is_geometric else 'No')