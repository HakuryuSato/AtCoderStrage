import sys
from decimal import Decimal, getcontext
getcontext().prec = 24

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def calc(x1, y1, x2, y2):
    dx = Decimal(x2) - Decimal(x1)
    dy = Decimal(y2) - Decimal(y1)
    return (dx**2 + dy**2).sqrt()


N = int(input())
coordinates = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(0, 0)]



result = 0
for i in range(len(coordinates) - 1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]
    result += calc(x1, y1, x2, y2)

print(result)
