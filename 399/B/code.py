import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


N=int(input())
P=read_list()
A=sorted(P,reverse=True)

for p in P:
    print(A.index(p)+1)
