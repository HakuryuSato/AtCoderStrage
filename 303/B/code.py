import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]

adjacency = set()

for lis in l:
    for i in range(len(lis) - 1):
        x, y = lis[i], lis[i + 1]
        adjacency.add((min(x, y), max(x, y)))

not_connected = 0
for x in range(1, N + 1):
    for y in range(x + 1, N + 1):
        if (x, y) not in adjacency:
            not_connected += 1

print(not_connected)
