import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

y = int(input())

if ((y % 4 == 0) and not (y % 100 == 0)) or (y % 400 == 0):
    print(366)
else:
    print(365)
