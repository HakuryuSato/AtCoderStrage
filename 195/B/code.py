import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

A,B,W = map(int,input().split())
W *= 1000


min_count = float('inf')
max_count = -float('inf')

for i in range(1, W // A + 1):
    if A * i <= W <= B * i:
        min_count = min(min_count, i)
        max_count = max(max_count, i)


if min_count == float('inf'):
    print("UNSATISFIABLE")
else:
    print(min_count, max_count)












'''
A以上B以下の整数から、
ちょうど W*10^3 を作ることができる最小値と最大値を求めよ

存在しない場合はUNSATISFIABLEと出力

入力例
120 150 2

出力例
14 16


'''