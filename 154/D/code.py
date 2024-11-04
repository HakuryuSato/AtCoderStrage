import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N, K = map(int, input().split())
p=list(map(int,input().split()))

expectation = [(x + 1) / 2 for x in p]

cumulative_sum = [0] * (N + 1)
for i in range(1, N + 1):
    cumulative_sum[i] = cumulative_sum[i - 1] + expectation[i - 1]

max_expectation = 0
for i in range(N - K + 1):
    current_sum = cumulative_sum[i + K] - cumulative_sum[i]
    max_expectation = max(max_expectation, current_sum)

print(max_expectation)



'''
K,N=1~2*10^5
pi=1~1000

隣接するK個のサイコロpiを振った時に出る目の期待値の最大値を出力
サイコロは1からpiまでの種類の目がそれぞれ等確立で出る

[私の考え]
数が小さいので全探索するだけでは？
pに対して、Kでループし、合計をmaxで比較し、出力？

ループ数が10^10になるので累積和が必要？

'''