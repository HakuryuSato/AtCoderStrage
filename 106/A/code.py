import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

n=int(input())

for i in range(1,38):
    for j in range (1,38):
        if 3**i + 5**j == n:
            print(f'{i} {j}')
            exit()


print(-1)