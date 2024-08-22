import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

S = list(map(int, input().split()))


a = sorted(S)
# print(a)

if a == S and all(s >= 100 and s <= 675 for s in S) and all(s % 25 == 0 for s in S):
    print("Yes")
else:
    print("No")
