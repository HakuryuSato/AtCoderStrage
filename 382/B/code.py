import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,D = map(int,input().split())
S = input()

for _ in range(D):
    S = S[::-1].replace('@', '.', 1)[::-1]
print(S)

