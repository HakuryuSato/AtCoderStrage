import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
l = [0] * N

for i in range(N):
    l[i] = list(map(int, input().split()))

i = 0
for j in range(N):
    if i - 1 >= j:
        i = l[i - 1][j]
    else:
        i = l[j][i - 1]

print(i)
