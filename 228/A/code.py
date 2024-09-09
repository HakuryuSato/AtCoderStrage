import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

S,T,X = map(int,input().split())

if S < T:
    print("Yes" if S <= X < T else "No")
else:
    print("Yes" if X >= S or X < T else "No")