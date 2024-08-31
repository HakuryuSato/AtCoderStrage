import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


A, B = map(int, input().split())

count = 0

for x in range(-200, 201):
    if (2 * B == A + x) or (2 * x == A + B) or (2 * A == B + x):
        count += 1

print(count)