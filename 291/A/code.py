import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

S=list(input())
for i in range(len(S)):
    if S[i].upper() == S[i]:
        print(i+1)
        exit()