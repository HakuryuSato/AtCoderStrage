import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N = int(input())

F = [[0]*2 for _ in range(N)]

for i in range(N):
    F[i]=list(map(int,input().split()))

F.sort(reverse=True,key=lambda x:x[1])
max_satisfaction = F[0][1] + F[1][1]

# 時間ないのでここまで、くやしい 
