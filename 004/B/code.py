import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 実行時間2秒 メモリ1GB

l=[]
for _ in range(4):
    l.append(input().split())

rotated = [row[::-1] for row in l[::-1]]
for row in rotated:
    print(' '.join(row))


