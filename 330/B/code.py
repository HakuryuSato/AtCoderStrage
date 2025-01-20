import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

result = []

for a in A:
    if L <= a <= R:
        result.append(a)
    else:
        if abs(L - a) <= abs(R - a):
            result.append(L)
        else:
            result.append(R)

print(*result)
