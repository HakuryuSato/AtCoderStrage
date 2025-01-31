import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__



n = int(input())
cnt = [0] * 24

for i in range(0, n):
    w, x = map(int, input().split())
    cnt[x] += w

ans = 0
for i in range(24):
    sum = 0
    for j in range(9):
        sum += cnt[(i + j) % 24]
    ans = max(ans, sum)

print(ans)

