import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
A = {int(input()) for _ in range(N)}

print(sorted(A, reverse=True)[1]) 



'''
実行時間2秒 メモリ1GB
[問題文]


[私の考え]

'''