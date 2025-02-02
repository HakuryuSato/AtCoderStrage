import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

M = int(input())
D = list(map(int, input().split()))

total_day = sum(D)

target_day = (total_day + 1) // 2

current_day_sum=0

for i in range(M):
    current_day_sum += D[i]
    if current_day_sum >= target_day:
        day_in_month = target_day - (current_day_sum - D[i])
        print (i + 1, day_in_month)
        break


