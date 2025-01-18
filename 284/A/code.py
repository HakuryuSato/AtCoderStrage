import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
l=[]
for _ in range(N):
    l.append(input())

for text in reversed(l):
    print(text)
