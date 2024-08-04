import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

n=input()
myset = set(map(int,input().split(' ')))


if(len(myset)>=2):
    print('No')
else:
    print('Yes')
