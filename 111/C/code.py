import sys
from collections import Counter

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n = int(input())
v=list(map(int,input().split()))

even_values = v[0::2]
odd_values = v[1::2]

even_counts = Counter(even_values)
odd_counts = Counter(odd_values)

even_most_common = even_counts.most_common(2) + [(None, 0)]
odd_most_common = odd_counts.most_common(2) + [(None, 0)]

if even_most_common[0][0] != odd_most_common[0][0]:
    changes = (len(even_values) - even_most_common[0][1]) + (len(odd_values) - odd_most_common[0][1])
else:
    changes1 = (len(even_values) - even_most_common[0][1]) + (len(odd_values) - odd_most_common[1][1])
    changes2 = (len(even_values) - even_most_common[1][1]) + (len(odd_values) - odd_most_common[0][1])
    changes = min(changes1, changes2)

print(changes)