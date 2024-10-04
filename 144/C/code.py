import sys
import math

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
min_moves = float('inf')

for i in range(1, int(math.sqrt(N)) + 1):
    if N % i == 0:
        j = N // i
        moves = (i - 1) + (j - 1)
        min_moves = min(min_moves, moves)

print(min_moves)


'''
問題
掛け算表のマスi,jには整数i*jが書かれており、最初1,1にいる
1会の移動でi,jからi+1,jかi,j+1のどちらかにのみ移動可能
整数Nが書かれているマスに到達するまでに必要な移動回数の最小値を求めよ
N=2~10^12

私の考え
桁が大きいので、対数関数などで指数を求めて移動する必要がある？
斜めの移動が指数関数的なので、それらから指数を求めて、
まずは大きく移動してから、最後の調整を行う？
→指数ではなく約数で良い

'''