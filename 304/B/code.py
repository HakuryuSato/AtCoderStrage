import sys

# # ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())


if N < (10**3):
    print(N)
else:
    digit = len(str(N))-1  # len-1がn乗
    factor = 10 ** (digit - 2)
    print((N // factor) * factor)
