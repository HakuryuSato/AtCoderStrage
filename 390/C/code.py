import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

H,W = map(int,input().split())
S=[list(input()) for _ in range(H)]

if len(S)

for i in range(H):
    for j in range(W):
        if