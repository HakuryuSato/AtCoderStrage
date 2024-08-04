import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

def calc(N):
    if N <= 0:
        return False
    while N % 2 == 0:
        N //= 2
    while N % 3 == 0:
        N //= 3
    return N == 1



N = int(input())

if(calc(N)):
    print('Yes')
else:
    print('No')


