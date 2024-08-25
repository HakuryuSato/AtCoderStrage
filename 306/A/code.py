import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input())
S = input()

l=[]
for s in S:
    l.append(s)
    l.append(s)


print("".join(l))

