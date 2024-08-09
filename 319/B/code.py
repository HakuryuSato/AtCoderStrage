import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())

result = ["-"] * (N + 1)
for i in range(N + 1):
    for j in range(1, 10):
        if N % j == 0 and i % (N // j) == 0:
            result[i] = str(j)
            break

print("".join(result))