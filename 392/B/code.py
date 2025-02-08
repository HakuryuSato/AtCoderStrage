import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M =map(int,input().split())
A=list(map(int,input().split()))

result=[]
for i in range(1,N+1):
    if not i in A:
        result.append(i)

print(len(result))
print(*result)