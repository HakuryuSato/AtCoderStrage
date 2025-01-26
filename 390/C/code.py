import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

min_row, max_row = H, -1
min_col, max_col = W, -1

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if S[i][j] == ".":
            print("No")
            exit()

print("Yes")
