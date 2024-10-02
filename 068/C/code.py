import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M=map(int,input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

neighbors_of_1 = set()
neighbors_of_N = set()

for a, b in edges:
    if a == 1:
        neighbors_of_1.add(b)
    elif b == 1:
        neighbors_of_1.add(a)
    if a == N:
        neighbors_of_N.add(b)
    elif b == N:
        neighbors_of_N.add(a)

if neighbors_of_1 & neighbors_of_N:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

