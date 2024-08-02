import sys

# ローカル用
file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


text = input()
x, y = map(int, text.split())


if -3 <= (y - x) <= 2:
    print("Yes")
else:
    print("No")
