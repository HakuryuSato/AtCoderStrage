import sys
from itertools import accumulate

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
A=list(map(int,input().split()))

S=list(accumulate(A))
S2=list(accumulate(x**2 for x in A))

total_sum = 0
for i in range(1, N):
    total_sum += i * A[i]**2 - 2 * A[i] * S[i-1] + S2[i-1]

print(total_sum)