import sys
from collections import deque
from itertools import accumulate


# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

Q = int(input())
l = []
idx = 0
start = 0

for i in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l.append(idx)
        idx += query[1]

    elif query[0] == 2:
        start += 1

    elif query[0] == 3:
        k = query[1] - 1
        print(l[start + k] - l[start])
