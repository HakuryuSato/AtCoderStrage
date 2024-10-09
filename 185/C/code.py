import sys
import math

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

L=int(input())

remainder = L - 12
print(math.comb(remainder + 11, 11))









'''
[問題文]
長さLの鉄の棒がある、
この棒を全て正整数となるように12本に分割する
方法は何通りあるか？
L=12~200

分割の方法は、例えば13の場合は12通りとなる(長さ2がどこに配置されるかによって区別される)

[私の考え]
割ったあまりの12乗？
場合分け？、12なら1、それ以上なら指数関数的に増加？

'''