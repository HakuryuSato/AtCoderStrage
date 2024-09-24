import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M,K = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

sum_A = [0] * (N+1)
sum_B = [0] * (M+1)

for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]

for i in range(M):
    sum_B[i+1] = sum_B[i] + B[i]

max_books = 0
j = M

for i in range(N+1):
    if sum_A[i] > K:
        break
    while j > 0 and sum_A[i] + sum_B[j] > K:
        j -= 1
    max_books = max(max_books, i + j)

print(max_books)
