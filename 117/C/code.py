import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M=map(int,input().split())
X=list(map(int,input().split()))

X.sort()

distances = []
for i in range(1, M):
    distances.append(X[i] - X[i - 1])

distances.sort(reverse=True)
min_moves = sum(distances[N - 1:])

print(min_moves)



# N=使えるコマの数 例:2 1~10^5
# M=到達する必要のある座標数 例：5  1~10^5
# X 数直線上にあるコマの座標 例：10 12 1 2 14   -10^5~10^5
# コマを置いた時、およびコマを前後１マス動かしたときに、座標に到達したことになる。
# 最小となるコマの移動数はいくつになるか？を出力 例:5


'''
私の考え
・まず、座標を昇順にする必要がある？
・座標間の差分を考える？
・Xの値が大きいので、二分探索などのアプローチが必要？
'''