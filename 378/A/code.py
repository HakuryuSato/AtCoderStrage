import sys
from collections import Counter

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

l=list(map(int,input().split()))

counter = Counter(l)
result = sum(count // 2 for count in counter.values())
print(result)