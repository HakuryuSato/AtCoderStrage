import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


n, s, t = map(int, input().split())
w = int(input())

best_count = 1 if s <= w <= t else 0

for _ in range(n - 1):
    w += int(input())
    best_count += 1 if s <= w <= t else 0

print(best_count)