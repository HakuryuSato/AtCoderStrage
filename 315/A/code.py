import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

S = input()
words = ["a", "e", "i", "o", "u"]

print("".join([char for char in S if char not in words]))
