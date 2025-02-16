import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


from collections import Counter

N = int(input())
A = read_list()
A_counter = Counter(A)

x, y = 0, 0


for num, count in sorted(A_counter.items(), reverse=True):
    if count >= 4:
        if x == 0:
            x = num
            y = num
        elif y == 0:
            y = num
        break
    elif count >= 2:
        if x == 0:
            x = num
        elif y == 0:
            y = num
            break

print(x * y)