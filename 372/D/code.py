import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N = int(input())
H = list(map(int, input().split()))

# 辞書で高さ管理？高さとインデックス？