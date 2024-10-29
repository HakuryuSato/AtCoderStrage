import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

S = list(input())
N=int(input())
queue = [tuple(map(int, input().split())) for _ in range(N)]

for left, right in queue:
    S[left-1:right] = S[left-1:right][::-1]

print("".join(S))