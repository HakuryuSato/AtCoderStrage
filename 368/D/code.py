import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N,K = map(int,input().split())
l  = [[0]*N for _ in range(N)]

for i in range(N):
    data = list(map(int,input().split()))
    l[data[0]][l[data[1]]]