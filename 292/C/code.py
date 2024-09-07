import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N=int(input())


ab_count = [0] * (N + 1)

for A in range(1, N + 1):
    for B in range(1, N // A + 1):
        ab_count[A * B] += 1

result = 0
for AB in range(1, N + 1):
    if N - AB >= 1:
        result += ab_count[AB] * ab_count[N - AB]



print(result)


