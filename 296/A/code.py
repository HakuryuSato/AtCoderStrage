import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
S = input()

print("Yes" if not(("MM" in S) or ("FF" in S)) else "No")
