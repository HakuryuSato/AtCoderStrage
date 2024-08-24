import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int,input().split()))


count = 0
A.sort(reverse=True)

def check(A):
    return  sum(1 for x in A if x > 0) <= 1

while(not check(A)):
    count+=1
    A[0]-=1
    A[1]-=1
    A.sort(reverse=True)
    


print(count)

