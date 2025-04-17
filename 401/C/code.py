import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

N,K = read_values()


s=K

# 一旦1で初期化する
A = [1 for i in range(N+1)]

for i in range(K,N+1):
    # kのフィボナッチ
    A[i]=s
    s-=A[i-K]
    s+=A[i]
    s%=1000000000

print(A[N])