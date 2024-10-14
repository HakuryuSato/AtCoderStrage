import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N = input().strip()

digits = list(N)
n = len(digits)
max_prod = 0

for mask in range(1, (1 << n) - 1):
    num1_digits = []
    num2_digits = []
    
    for i in range(n):
        if mask & (1 << i):
            num1_digits.append(digits[i])
        else:
            num2_digits.append(digits[i])

    num1_sorted = sorted(num1_digits, reverse=True)
    num2_sorted = sorted(num2_digits, reverse=True)
    

    if num1_sorted[0] == '0' or num2_sorted[0] == '0':
        continue

    num1 = int(''.join(num1_sorted))
    num2 = int(''.join(num2_sorted))

    prod = num1 * num2
    if prod > max_prod:
        max_prod = prod

# 結果を出力
print(max_prod)

'''
実行時間2秒 メモリ1GB
[問題文]
1~10^9のNが与えられる、
Nから正整数として２つに分離したとき、
分離後の２数の積の最大値はいくらになるか？
*正整数なので0が含まれてはならない

入力例,出力例
123,63

1010,100


[私の考え]
標準ライブラリで組み合わせ生成？
積の最大値を求めたいので、桁の中心で区切る方が良い？
→NG

ビットマスクで全探索？

'''