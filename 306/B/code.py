import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

A = list(map(int,input().split()))

sum=0

for i in range(len(A)):
    if(A[i]==1):
        sum += 2**i
print(sum)