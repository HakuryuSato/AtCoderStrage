import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
S=input()

result =0
for i in range(N-2):
    if S[i] == '#' and S[i+1]=='.' and S[i+2]=='#':
        result+=1

print(result)