import sys

# ローカル用
file_number = 2
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__


N = int(input())
H = list(map(int, input().split()))


T=0
for health in H:
    while health > 0:
        T += 1
        if T % 3 == 0:
            health -= 3
        else:
            health -= 1

# T = sum((2 * h + 2) // 3 for h in H)
print(T)