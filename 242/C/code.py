import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
MOD = 998244353
dp = [[0] * 10 for _ in range(N + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(1, 10):

        dp[i][j] = dp[i - 1][j]
        if j > 1:
            dp[i][j] += dp[i - 1][j - 1]
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]
        dp[i][j] %= MOD

result = sum(dp[N][j] for j in range(1, 10)) % MOD

print(result)
