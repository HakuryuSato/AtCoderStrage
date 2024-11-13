import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=input().strip()

print(N[1] + N[2] + N[0],N[2] + N[0] + N[1])