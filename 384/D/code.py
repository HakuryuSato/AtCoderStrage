import sys
from itertools import accumulate

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N,S = map(int,input().split())
A=list(map(int,input().split()))

# print('Yes' if any(S%a==0 for a in A) else 'No')

flag=False

dp=1
for a in A:
    dp = 
