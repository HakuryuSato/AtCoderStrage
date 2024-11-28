import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
S = input()

mid = N // 2
if N % 2 == 1 and S[:mid] == "1" * mid and S[mid] == "/" and S[mid + 1 :] == "2" * mid:
    print("Yes")
else:
    print("No")



