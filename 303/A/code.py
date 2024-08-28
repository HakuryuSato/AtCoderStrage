import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
S=input()
T=input()

result = True
for i in range(N):
    if not((S[i] == T[i]) or (S[i]=='1' and T[i]=='l') or  (S[i]=='l' and T[i]=='1') or (S[i]=='0' and T[i]=='o') or (S[i]=='o' and T[i]=='0')):
        result = False


print('Yes' if result else 'No')
