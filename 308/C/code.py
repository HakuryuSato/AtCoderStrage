import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

def calc(l):
    return l[0]/(l[0]+l[1])

N=int(input())

data = N* [0]

for i in range(N):
    data[i] = i+1,calc(list(map(int,input().split())))

sorted_result = sorted(data, key=lambda x: (-x[1], x[0]))

print(*[x[0] for x in sorted_result])