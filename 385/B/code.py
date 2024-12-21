import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

H, W, X, Y = map(int, input().split())
S = [""] + [[""] + list(input()) for _ in range(H)]
T = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


current = (X, Y)
home = set()

for t in T:
    dx, dy = directions[t]
    next_x, next_y = current[0] + dx, current[1] + dy

    if 1 <= next_x <= H and 1 <= next_y <= W and S[next_x][next_y] != "#":
        current = (next_x, next_y)

        if S[current[0]][current[1]] == "@":
            home.add(current)


print(*current, len(home))
