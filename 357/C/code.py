import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


N = int(input())


def generate_carpet(prev_carpet):
    size = len(prev_carpet)
    new_carpet = []
    
    for i in range(3 * size):
        if size <= i < 2 * size:
            new_carpet.append(prev_carpet[i % size] + '.' * size + prev_carpet[i % size])
        else:
            new_carpet.append(prev_carpet[i % size] * 3)
    
    return new_carpet


carpet = ['#']
for _ in range(N):
    carpet = generate_carpet(carpet)

print("\n".join(carpet))




'''
実行時間2秒 メモリ1GB
[問題文]
レベルNのカーペットを出力する

レベル0:黒いマス(#) 1マスからなる1x1のグリッド
K>0のとき、レベルNのカーペットは3^N*3^Nのグリッドである、
このグリッドを3^N-1x3^N-1のブロック9個に分割したとき、
・中央のブロックは全て白いマスからなす、
・他の8個のブロックはレベル(K-1)のカーペットである
N=0~6

入力例
2


出力例
#########
#.##.##.#
#########
###...###
#.#...#.#
###...###
#########
#.##.##.#
#########



[私の考え]
標準ライブラリなどで、簡単に作れないか？

'''