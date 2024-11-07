import sys
from collections import defaultdict
from itertools import combinations

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

nums = list(map(int, input().split()))
sums = defaultdict(int)

sum_list = sorted(set(sum(comb) for comb in combinations(nums, 3)), reverse=True)

print(sum_list[2])