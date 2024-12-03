import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

S = list(input())


for i in range(1, len(S), 2):
    S[i], S[i - 1] = S[i - 1], S[i]

print(''.join(S))