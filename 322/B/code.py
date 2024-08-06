import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


def check(N, M, S, T):
    prefix = T[:N]
    suffix = T[-N:]
    if prefix == S and suffix == S:
        return 0
    elif prefix == S:
        return 1
    elif suffix == S:
        return 2
    else:
        return 3


N, M = map(int, input().split())
S = str(input())
T = str(input())

print(check(N,M,S,T))