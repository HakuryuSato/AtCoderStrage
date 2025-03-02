import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

def read_values():
    return map(int, input().split())

def read_list():
    return list(read_values())



from collections import defaultdict
N = int(input())
A = read_values()

data = defaultdict(list)
ans=10**6

for idx, a in enumerate(A): # 10^5
    data[a].append(idx)

for val in data:
    positions = data[val]
    if len(positions) >= 2:

        for i in range(len(positions) - 1):
            ans = min(ans, positions[i+1] - positions[i])

print(ans+1 if ans != 10**6 else '-1')

