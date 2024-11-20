import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

S = input().strip('|').split('|') 
result = [s.count('-') for s in S] 
print(*result)