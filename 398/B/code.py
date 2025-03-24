import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

from collections import Counter

cards = list(map(int, read_list()))
count = Counter(cards)
freqs = sorted(count.values(), reverse=True)

if len(freqs) >= 2 and freqs[0] >= 3 and freqs[1] >= 2:
    print("Yes")
else:
    print("No")