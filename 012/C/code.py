import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

N=int(input())
num = 2025-N

for i in range(10):
    for j in range(10):
        if i * j == num:
            print(f'{i} x {j}')
