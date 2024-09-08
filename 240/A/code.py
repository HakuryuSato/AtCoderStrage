import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

a,b=map(int,input().split())

if(b-a==1 or b-a==9):
    print('Yes')
else:
    print('No')




