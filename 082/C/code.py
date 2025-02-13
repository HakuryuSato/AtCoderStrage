import sys

# ローカル用
# file_number = 5
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

from collections import Counter

n=int(input())
A=read_list()
A=Counter(A)

ans = 0

for i in A:
    if A[i] >= i:
         ans += A[i] - i
    else:
         ans += A[i]
print(ans)