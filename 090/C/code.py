import sys

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N,M = map(int,input().split())

if N == 1:
    if M == 1:
        ans = 1
    else:
        ans = M - 2
else:
    ans = (N - 2) * (M - 2)
print(ans)