import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M=map(int,input().split())
knight_positions = [tuple(map(int, input().split())) for _ in range(M)]

knight_moves = [
    (-2, -1), (-2, 1), (2, -1), (2, 1),
    (-1, -2), (-1, 2), (1, -2), (1, 2)
]


unsafe_positions = set()

for x, y in knight_positions:
    unsafe_positions.add((x, y)) 
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= N: 
            unsafe_positions.add((nx, ny))

total_positions = N * N
safe_positions_count = total_positions - len(unsafe_positions)

print(safe_positions_count)


'''
実行時間2秒 メモリ1GB制限

[問題文]
先ほどの問題に似ているが、先ほどの#の挙動がチェスのルークだとすると、
次の問題ではチェスのナイトのように動作する。

また、#がコマの位置ではなく、座標が与えられる。
最初の1行はデータ量を表すNとMが入る。

入力例
8 6
1 4
2 1
3 8
4 5
5 2
8 3

出力例
38

制約
N=1~10^9
M=1~2*10^5


'''