import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

sum = 0
for b in B:
    sum+=A[b-1]
print(sum)