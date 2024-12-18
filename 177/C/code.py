import sys
from itertools import accumulate

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int,input().split()))

mod = 10**9 + 7
A_accumulate = list(accumulate(A))
result = 0

for i in range(N-1):
    result = (result + (A[i] * (A_accumulate[N-1] - A_accumulate[i]))) % mod

print(result)


