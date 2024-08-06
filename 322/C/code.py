import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [-1 for _ in A]

for i in range(N):
    if(i in A and A.index(i)==i):
        print(0)
    else:
        # ここで二分探索を書けば良かった、時間なかったのでギブ。