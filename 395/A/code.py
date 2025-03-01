import sys

# ローカル用
# file_number = 1

# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


N=int(input())
A=read_list()


for i in range(N-1):
    if A[i] >= A[i+1]:
        print('No')
        exit()



print('Yes')