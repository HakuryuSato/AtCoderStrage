import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,T=map(int,input().split())
A=[int(input()) for _ in range(N)]


total_time = 0
door_close_time = 0

for i in range(N - 1):
    total_time += min(T, A[i + 1] - A[i])

total_time += T

print(total_time)


'''
実行時間2秒 メモリ1GB
[問題文]
N人(1~10^5)の人が自動ドアを通り過ぎた、
自動ドアはT(1~10^5)秒の間あいており、閉じる前に人が通過すると時間が延長される
Aは人が通り過ぎた時刻(1~10^5)である。

ドアが開いていた合計秒数は？

入力例
5 10
20
100
105
217
314


出力例
45

[私の考え]
Aでループし、人が通過した時間の間隔がT秒未満かどうかを判定、
未満ならばその時間、そうでないならばT秒として合計に可算して出力

'''