import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

s = input().strip()
n = len(s)
m = sum(map(int, s)) % 3
c = [0, 0, 0]
for x in s:
    c[int(x) % 3] += 1

if m == 0:
    print(0)
elif c[m] >= 1 and n > 1:
    print(1)
elif c[3 - m] >= 2 and n > 2:
    print(2)
else:
    print(-1)

