import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# 提出用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# マス番号と石の個数をソート
stones = sorted(zip(X, A))
sum_stones = 0 
sum_indices = 0

# stonesでループして石が足りるか+石合計+マスインデックス合計
for x, a in stones:
    if sum_stones < x - 1:  # 必要な石が足りない場合
        print(-1)
        exit()
    sum_stones += a
    sum_indices += x * a

# 石の総数がちょうどN
if sum_stones != N:
    print(-1)
    exit()

target_sum = N * (N + 1) // 2
print(target_sum - sum_indices)