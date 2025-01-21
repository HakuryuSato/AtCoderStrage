import sys
import math

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

X=int(input())

factorial = 1
for N in range(1, 21):
    factorial *= N
    if factorial == X:
        print(N)
        break

