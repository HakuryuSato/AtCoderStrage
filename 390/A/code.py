import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

A = list(map(int, input().split()))
B = [1, 2, 3, 4, 5]

result = 'No'
for i in range(len(A) - 1):
    A[i], A[i + 1] = A[i + 1], A[i]
    if A == B:
        result = 'Yes'
    A[i], A[i + 1] = A[i + 1], A[i]
print(result)