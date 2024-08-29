import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

H,W = map(int,input().split()) # H=6 W=6
l=[] 


for i in range(H):
    l.append(list(input().split()))

directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
target = "snuke"
result = []

for i in range(H):
    for j in range(W):
        if l[i][0][j] == 's':
            for dx, dy in directions:
                found = True
                for k in range(len(target)):
                    ni, nj = i + dx * k, j + dy * k
                    if ni < 0 or ni >= H or nj < 0 or nj >= W:
                        found = False
                        break
                    if l[ni][0][nj] != target[k]:
                        found = False
                        break
                if found:
                    for k in range(len(target)):
                        ni, nj = i + dx * k, j + dy * k
                        result.append((ni + 1, nj + 1))

for x, y in result:
    print(x, y)
