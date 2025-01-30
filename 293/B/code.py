import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int, input().split()))

flag = [False] * N

for idx,a in enumerate(A):
    if flag[idx]==True:continue

    flag[a-1] = True

result = [idx+1 for idx in range(N) if not flag[idx]]  # 1 から N まで調べる

print(len(result))
print(*result)