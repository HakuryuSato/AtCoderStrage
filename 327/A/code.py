import sys

# # ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")


sys.stdin = sys.__stdin__ # 本番用


N = input()
s = input()

if "ab" in s or "ba" in s:
    print("Yes")
else:
    print("No")
