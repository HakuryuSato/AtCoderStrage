import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
H, W, K = read_values()
GRID = [list(input()) for _ in range(H)]
ans = 0
visited = [[False] * W for _ in range(H)]


def recursive(i, j, k):
    global ans
    if k == K:
        ans += 1
        return
    
    visited[i][j]=True

    for direction_i, direction_j in directions:
        next_i = i + direction_i
        next_j = j + direction_j

        if (
            0 <= next_i < H
            and 0 <= next_j < W
            and GRID[next_i][next_j] == "."
            and not visited[next_i][next_j]
        ):
            recursive(next_i, next_j, k + 1)

    visited[i][j] = False


for i in range(H):
    for j in range(W):
        # start i,j
        path = []

        if GRID[i][j] == ".":
            recursive(i, j, 0)

print(ans)