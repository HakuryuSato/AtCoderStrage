import sys

# ローカル用
file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

n = int(input())


for i in range(n, 920):
    a, b, c = map(int, str(i))
    if a * b == c:

        print(str(i))
        break
