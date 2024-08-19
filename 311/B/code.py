import sys

# ローカル用
file_number = 5
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, D = map(int, input().split())
S = []

for i in range(N):
    S.append(input().strip())

streak = 0
max_streak = 0
for col in range(D):
    if all(row[col] == "o" for row in S):
        streak += 1
        max_streak = max(streak, max_streak)
    else:
        streak = 0  # 連続が途切れたら初期化
print(max_streak)
