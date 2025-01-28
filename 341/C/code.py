import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

h, w, n = map(int, input().split())
T = list(input())
GRID = [list(input()) for _ in range(h)]


def directions(t, i, j):
    if t == "L":
        return i, j - 1
    elif t == "R":
        return i, j + 1
    elif t == "U":
        return i - 1, j
    elif t == "D":
        return i + 1, j


def check(T, i, j):
    for idx, t in enumerate(T):
        next_i, next_j = directions(t, i, j)
        if 0 <= next_i < h and 0 <= next_j < w:
            i, j = next_i, next_j
            if GRID[next_i][next_j] == ".":
                if idx == n - 1:
                    return True
            else:
                return False
        else:
            return False


result = 0
for i in range(h):
    for j in range(w):
        if GRID[i][j] == ".":
            if check(T, i, j):
                result += 1

print(result)
