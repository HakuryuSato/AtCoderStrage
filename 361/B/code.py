import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

Ax1,Ay1,Az1,Ax2,Ay2,Az2 = map(int, input().split())
Bx1,By1,Bz1,Bx2,By2,Bz2 = map(int, input().split())

def check(l1, r1, l2, r2):
    return not (r1 <= l2 or r2 <= l1)


if check(Ax1, Ax2, Bx1, Bx2) and check(Ay1, Ay2, By1, By2) and check(Az1, Az2, Bz1, Bz2):
    print("Yes")
else:
    print("No")