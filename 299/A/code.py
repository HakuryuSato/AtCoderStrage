import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input())

S=input()

start = S.find('|')
end = S.rfind('|')

if '*' in S[start:end]:
    print('in')
else:
    print('out')



