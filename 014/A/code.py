import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


a, b, c = map(int, input().split())

seen = set()
seen.add((a, b, c))

count = 0

while True:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print(count)
        break

    if (a, b, c) in seen and count > 0:
        print(-1)
        break

    seen.add((a, b, c))

    count += 1

    na = b // 2 + c // 2
    nb = a // 2 + c // 2
    nc = a // 2 + b // 2

    a, b, c = na, nb, nc