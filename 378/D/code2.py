import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


H, W, K = read_values()
S = [list(input()) for _ in range(H)]

ans = 0
visited = [[False] * W for _ in range(H)]


def rec(i, j, k):
    global ans
    if k == K:
        ans += 1
        return

    visited[i][j] = True

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "." and not visited[ni][nj]:
            rec(ni, nj, k + 1)

    visited[i][j] = False


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            rec(i, j, 0)

print(ans)
