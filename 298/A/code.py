import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 実行時間2秒 メモリ1GB

N=int(input())
S=input()

if ('o' in S) and (not 'x' in S):
    print('Yes')
else:
    print('No')

