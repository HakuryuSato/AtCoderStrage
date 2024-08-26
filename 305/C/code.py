import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

H,W = map(int,input().split())
grid=[]
for i in range(H):
    grid.append(list(input().strip())) 

def check(grid):
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and (
                (i > 0 and grid[i-1][j] == '#') or
                (i < H-1 and grid[i+1][j] == '#') or
                (j > 0 and grid[i][j-1] == '#') or
                (j < W-1 and grid[i][j+1] == '#')
            ):
                return i, j  # 最初に見つけた位置を返す

missing_hash = check(grid)

print(missing_hash)

