import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# 本番用
sys.stdin = sys.__stdin__


def canDistribute(x, A, M):
    total = sum(min(x, a) for a in A)
    return total <= M

def findMaxX(A, M):
    low, high = 1, max(A)
    while low < high:
        mid = (low + high + 1) // 2 
        if canDistribute(mid, A, M):
            low = mid 
        else:
            high = mid - 1 
    return low


N,M = map(int, input().split())
A = list(map(int, input().split()))

total_sum = sum(A)
if total_sum <= M:
    print("infinite")
else:
    result = findMaxX(A, M)
    print(result)
