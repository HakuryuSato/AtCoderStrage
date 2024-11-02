import sys


# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')


# # 提出用
sys.stdin = sys.__stdin__

from collections import deque

query = list(map(int, sys.stdin.read().split()))
Q = query[0]
query = query[1:]

tube = deque()
result = []

i = 0
while i < len(query):
    q_type = query[i]
    if q_type == 1:
        x = query[i + 1]
        c = query[i + 2]
        if tube and tube[-1][0] == x:
            tube[-1] = (x, tube[-1][1] + c)
        else:
            tube.append((x, c))
        i += 3
    elif q_type == 2:
        c = query[i + 1]
        total_sum = 0
        while c > 0:
            x, count = tube[0]
            if count <= c:
                total_sum += x * count
                c -= count
                tube.popleft()
            else:
                total_sum += x * c
                tube[0] = (x, count - c)
                c = 0
        print(total_sum)
        i += 2



'''
問題文の読解ミスで時間使った、
同じ数字分を追加で格納するので、ランレングス圧縮が最適

'''