import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# 提出用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# XZ合わせてソート
stones = sorted(zip(X, A))

sum_stones = 0
sum_indices = 0

# 各stonesのxzに対して、x-1の個数がsum stones以下ならば足りないので終了、
for x, a in stones:
    if sum_stones < x - 1:
        print(-1)
        exit()
    sum_stones += a
    sum_indices += x * a

# 石の総数がNと一致しないならば終了
if sum_stones != N:
    print(-1)
    exit()

# total stonesからsum indices?を引いた回数が操作回数
total_stones = N * (N + 1) // 2
print(total_stones - sum_indices)
