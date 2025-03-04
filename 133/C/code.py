import sys
import numpy as np

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


L, R = read_values()

MOD = 2019
R = min(R, L + MOD)

result = MOD
for i in range(L, R):
    for j in range(i + 1, R + 1):
        result = min(result, (i * j) % MOD)
        if result == 0:
            print(0)
            exit()

print(result)


