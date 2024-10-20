import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
expressible_numbers = set()

for a in range(2, int(N**0.5) + 1):
    b = 2
    while (power := a ** b) <= N:
        expressible_numbers.add(power)
        b += 1

result = N - len(expressible_numbers)
print(result)


'''
実行時間2秒 メモリ1GB
[問題文]
整数Nが与えられる、1以上N以下の整数のうち、
2以上の整数a,bを用いてa^bとあらわせないものはいくつあるか？
N=1~10^10


[私の考え]
・Nが大きいので全探索はまず無理？
・"表せないもの"を数える点に注意
・Nを表せるa^bの組み合わせは、2~Nの整数から作ることができる

標準ライブラリで対数関数を使う？
collectionsでも解けるか？

'''