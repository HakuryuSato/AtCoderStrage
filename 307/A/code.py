import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int, input().split()))

result = []
sum = 0

for i in range(len(A)):
    sum += A[i]
    if (i + 1) % 7 == 0:
        result.append(sum)
        sum = 0

        

print(*result)
