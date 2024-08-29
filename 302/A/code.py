import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

a, b = map(int, input().split())

if(a%b==0):
    print(a//b)
else:
    print(a // b + 1)
