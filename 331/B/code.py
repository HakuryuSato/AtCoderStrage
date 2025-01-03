import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n,s,m,l = map(int,input().split())

INF = 10**9
dp = [INF] * (n + 12)
dp[0] = 0

for size, price in [(6, s), (8, m), (12, l)]:
    for i in range(n + 1):
        if i + size <= n + 11:
            dp[i + size] = min(dp[i + size], dp[i] + price)

print(min(dp[n:]))