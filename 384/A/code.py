import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,c1,c2=input().split()
S=list(input())

for i in range(int(N)):
    if S[i]!=c1:
        S[i]=c2

print(''.join(S))