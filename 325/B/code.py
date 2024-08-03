import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__


# 0時+xiが9~18に含まれるかどうか？ ずれの限界？



n = int(input())
cnt = [0 for _ in range(24)] # 空の配列作成
for i in range(0, n): # 0~nまでループ *値の格納用
    w, x = map(int, input().split())
    cnt[x] += w
ans = 0
for i in range(24):
    sum = 0
    for j in range(9):
        sum += cnt[(i + j) % 24]
    ans = max(ans, sum)

print(ans)

