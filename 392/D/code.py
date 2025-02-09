import sys


# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())



import numpy as np
n = int(input())
a = list()
k = list()

for _ in range(n):  # 200
    r = read_list()
    add = np.array([0] * 100001)  # add=追加する行, サイコロごとに10^5 で初期化
    k.append(r[0])
    for i in range(r[0]):  # 出目数(*出目ごとにループしてもループ数は一緒)
        add[r[i + 1]] += 1  # add[出目番号]=回数 という配列
    a.append(add)

   
ans = 0.0
for i in range(n):
    for j in range(i + 1, n):  # 全サイコロでループ、順序不要なのでi,jだけで良い
        sum = np.dot(a[i], a[j])  # 内積を計算
        ans = max(sum / (k[i] * k[j]), ans)  # 最大値比較


print(ans)
