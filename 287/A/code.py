import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
S=[input() for _ in range(N)]

if S.count('For') > S.count('Against'):
    print('Yes')
else:
    print('No')