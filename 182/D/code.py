import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


