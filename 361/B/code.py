import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# 提出用
sys.stdin = sys.__stdin__

x1, y1, z1, x2, y2, z2 = map(int, input().split())
x3, y3, z3, x4, y4, z4 = map(int, input().split())

def is_overlapping(a1, a2, b1, b2):
    return a1 < b2 and a2 > b1

print(
    "Yes"
    if is_overlapping(x1, x2, x3, x4)
    and is_overlapping(y1, y2, y3, y4)
    and is_overlapping(z1, z2, z3, z4)
    else "No"
)

