# ローカル用
import sys

# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())

C = [0] * (N + 1)
A = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    C[i] = int(input())
    A[i] = list(map(int, input().split()))

X = int(input())

vec = []
for i in range(1, N + 1):
    if X in A[i]:
        vec.append(i)

if vec:
    min_bet = min([C[i] for i in vec])
    result = [i for i in vec if C[i] == min_bet]
    print(len(result))
    print(" ".join(map(str, result)))
else:
    print(0)
