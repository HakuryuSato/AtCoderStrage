import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

def check(S):
    for i in range(1,17,2):

        if(S[i]=='1'):
            return 'No'
    return 'Yes'

S=input()

print(check(S))


