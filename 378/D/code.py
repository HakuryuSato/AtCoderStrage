import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
# sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
H, W, K = read_values()
GRID = [list(input()) for _ in range(H)]

dp = {}


def recursive(i, j, path):

    
    if path in dp:
        return dp[path]

    queue = []

    for direction in directions:
        next_i = i + direction[0]
        next_j = j + directions[1]

        if 0 <= next_i <=H and 0<= next_j <=W:
            queue.append(next_i,next_j)
    
    


for i in range(H):
    for j in range(W):
        # start i,j
        path = []

        if GRID[i, j] == "#":
            continue
