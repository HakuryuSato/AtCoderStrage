import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

# 2にたどり着けるかどうか。
# Nまでiが増加したら-1

N = int(input())
l = [0] * (N + 1)


for i in range(1, N + 1):
    l[i] = int(input())


current = l[1] 
count = 1  

for i in range(1, N + 1):
    if current == 2:  
        print(count)
        break
    elif i == N:  
        print(-1)
        break
    current = l[current] 
    count += 1
