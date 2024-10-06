import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


d,n = map(int,input().split())

count = 0
current = 1

while True:
    if current % (100 ** d) == 0 and current % (100 ** (d + 1)) != 0:
        count += 1
        if count == n:
            print(current)
            break
    current += 1
