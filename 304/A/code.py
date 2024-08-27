import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


N = int(input())

min_age=float('inf')
l = N*[0]
for i in range(N):
    text = input().split()
    l[i]=[text[0],int(text[1])]
    min_age = min(l[i][1],min_age)


start = next(i for i, row in enumerate(l) if row[1] == min_age)

result = l[start:] + l[:start]
for i in range(len(result)):
    print(result[i][0])