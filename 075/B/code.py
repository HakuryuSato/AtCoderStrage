import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__




H,W=map(int,input().split())

grid = [list(input()) for _ in range(H)]
result = [[0] * W for _ in range(H)]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            result[i][j] = '#'
        else:
            count = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                    count += 1
            result[i][j] = str(count)

# 結果を出力
for row in result:
    print(''.join(row))

'''
実行時間2秒 メモリ1GB
[問題文]
マインスイーパーのプログラムを書いてください
.は空きマス、#は爆弾マス
各マスから8方向に爆弾マスが何個あるかを出力する

[['.', '.', '.', '.', '.'], ['.', '#', '.', '#', '.'], ['.', '.', '.', '.', '.']]

入力例
3 5
.....
.#.#.
.....


出力例
11211
1#2#1
11211


[私の考え]
移動を簡略化する配列か関数を作成
新たな辞書に値を格納

'''