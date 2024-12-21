import sys
from collections import defaultdict

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
H=list(map(int,input().split()))

nums = defaultdict(set)

for i,h in enumerate(H):
    nums[h].add(i)
max_length = 1

for indices in nums.values():
    indices = sorted(indices)
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            diff = indices[j] - indices[i]
            length = 2
            current = indices[j]

            while current + diff in indices:
                current += diff
                length += 1

            max_length = max(max_length, length)

print(max_length)