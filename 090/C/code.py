import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N_input,M_input = map(int,input().split())

if N_input<M_input:
    N=N_input
    M=M_input
else:
    N=M_input
    M=N_input


if N == 1:
    if M == 1:
        ans = 1
    else:
        ans = M - 2
else:
    ans = (N - 2) * (M - 2)
print(ans)