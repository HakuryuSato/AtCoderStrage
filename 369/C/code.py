import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input()) #4
A=list(map(int,input().split())) #[3, 6, 9, 3]




count = N  
start = 0

while start < N - 1:
    d = A[start + 1] - A[start]
    end = start + 1
    
    while end + 1 < N and A[end + 1] - A[end] == d:
        end += 1
    

    length = end - start + 1
    count += (length * (length - 1)) // 2  

    start = end 

print(count)