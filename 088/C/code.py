import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

grid = [list(map(int, input().split())) for _ in range(3)]

is_possible = True


for i in range(1, 3):
    if (grid[i][0] - grid[0][0] != grid[i][1] - grid[0][1]) or (grid[i][0] - grid[0][0] != grid[i][2] - grid[0][2]):
        is_possible = False
        break


if is_possible:
    for j in range(1, 3):
        if (grid[0][j] - grid[0][0] != grid[1][j] - grid[1][0]) or (grid[0][j] - grid[0][0] != grid[2][j] - grid[2][0]):
            is_possible = False
            break

print("Yes" if is_possible else "No")

