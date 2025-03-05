import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

from itertools import combinations

n,m = read_values()
for l in combinations(range(1,m+1),n):
    print(*l, sep=' ')

    