import sys


# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int, input().split()))

sub = {}
B = []
for i in range(N):
    if A[i] in sub:
        B.append(sub[A[i]])
    else:
        B.append(-1)

    sub[A[i]] = i+1

print(*B)
