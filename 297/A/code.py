import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n,d=map(int,input().split())
T=list(map(int,input().split()))

result=False
for i in range(n-1):
    if T[i+1]-T[i] <= d:
        print(T[i+1])
        exit()

print(-1)