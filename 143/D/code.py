import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


n = int(input())
L = list(map(int, input().split()))
L.sort()

count = 0

for c in range(n - 1, 1, -1):
    a, b = 0, c - 1
    while a < b:
        if L[a] + L[b] > L[c]:

            count += b - a
            b -= 1
        else:
            a += 1

print(count)









'''
実行時間2秒 メモリ1GB
[問題文]
N本(3~2*10^3)の棒があり、i本目の棒の長さはLi(1~10^3)
以下条件を満たす3本の棒で三角形を作る時、作れる三角形は何種類あるか？
a<b+c
b<c+a
C<a+b

入力例
7
218 786 704 233 645 728 389

出力例
23


[私の考え]
予めソートして全探索？

'''