import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

grid = [input().strip() for _ in range(8)]

rows_with_hash = {i for i in range(8) if '#' in grid[i]}
cols_with_hash = {j for j in range(8) if any(grid[i][j] == '#' for i in range(8))}


dot_count = sum(1 for i in range(8) for j in range(8)
                if i not in rows_with_hash and j not in cols_with_hash and grid[i][j] == '.')

print(dot_count)