import sys
from bisect import bisect_right

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
A=list(map(int,input().split()))

res=0

for i in range(1,N):
    idx = bisect_right(A,A[i]/2)
    res+=idx

print(res)