import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

sum=0
for color in C:
    if(color in D):
        sum+=P[D.index(color)+1]
    else:
        sum += P[0]

print(sum)