import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, Q = map(int, input().split())
moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
A = [(i + 1, 0) for i in range(N)][::-1]
for _ in range(Q):
    T, C = input().split()
    if T == "1":
        x, y = A[-1]
        dx, dy = moves[C]
        x += dx
        y += dy
        A.append((x, y))
    else:
        print(*A[-int(C)])