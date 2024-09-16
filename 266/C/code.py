import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


l = [list(map(int, input().split())) for _ in range(4)]

def is_convex(l):
    for i in range(4):
        x1, y1 = l[i]
        x2, y2 = l[(i + 1) % 4]
        x3, y3 = l[(i + 2) % 4]
        if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) <= 0:
            return "No"
    return "Yes"

print(is_convex(l))