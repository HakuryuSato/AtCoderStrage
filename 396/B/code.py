import sys
from collections import deque

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

Q = int(input())

cards = deque([0]*100)

for _ in range(Q):
    data = input().split()
    if data[0] == '1':
        x = int(data[1])
        cards.appendleft(x)
    else:
        top = cards.popleft()
        print(top)
