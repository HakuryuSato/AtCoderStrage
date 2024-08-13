import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

life = 0
for augment in P:
    if H + augment >= X:
        print(P.index(augment) + 1)
        break

