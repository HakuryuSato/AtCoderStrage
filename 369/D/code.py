import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N=int(input()) #5
A=list(map(int,input().split())) #[1, 5, 3, 2, 7]


#出力例 28



# 強い順に経験値を計算
dp_odd = 0  # 奇数回目で終わる場合の最大経験値
dp_even = 0  # 偶数回目で終わる場合の最大経験値

for i in range(N):
    new_dp_odd = max(dp_odd, dp_even + A[i])  # i番目を倒して奇数回目で終わる場合
    new_dp_even = max(dp_even, dp_odd + A[i] * 2)  # i番目を倒して偶数回目で終わる場合
    dp_odd, dp_even = new_dp_odd, new_dp_even  # 値を更新

print(max(dp_odd, dp_even))
