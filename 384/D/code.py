import sys
from itertools import accumulate

# ローカル用
file_number = 4
sys.stdin = open(f'input{file_number}.txt', 'r')

# 提出用
input = sys.stdin.readline


N, S = map(int, input().split())
A = list(map(int, input().split()))

# 1周期の最大はAの総和なので、約数で丸める
X = sum(A) # 2*10^5
S %= X

# Aを繰り返して拡張(組み合わせを増やすため？)
A += A # 2N= 4*10^5

# prefix sum 計算
prefix_sums = [0] + list(accumulate(A))
prefix_set = set(prefix_sums)

for p in prefix_sums: # 4*10^5
    # 累積和A[l]+A[r]=Sr-Sl-1
    # S=Sr-Sl-1
    # 変形すると Sr=S+Sl-1 -> p+SでSrになれば、証明できる
    if (p + S) in prefix_set: # set空の検索なのでO(1)
        print("Yes")
        break
else:
    print("No")


