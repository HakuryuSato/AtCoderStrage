import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

print(min(P,Q+min(D)))
