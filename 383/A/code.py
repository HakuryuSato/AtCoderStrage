import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())

water = 0
prev = 0

for _ in range(N):
    t, v = map(int, input().split())
    time = t-prev
    if water - time < 0:
        water = 0
    else:
        water -= time

    water += v
    prev = t

print(water)
