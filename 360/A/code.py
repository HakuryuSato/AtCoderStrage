import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

S=input()

if(S.index('R')<S.index('M')):
    print('Yes')
else:
    print('No')