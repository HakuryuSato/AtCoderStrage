import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

n,k = read_values()
A = list(read_values())

for _ in range(k):
    A.pop(0)
    A.append(0)
    
print(*A)