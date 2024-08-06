import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


def check(S):
    if "ABC" in S:
        return S.index("ABC") + 1
    else:
        return -1


N = int(input())
S = str(input())

print(check(S))
