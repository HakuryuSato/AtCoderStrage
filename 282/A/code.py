import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

k=int(input())

res = "".join(chr(i + ord('A')) for i in range(k))

print(res)