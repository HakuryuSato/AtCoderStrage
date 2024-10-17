import sys
import math

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, D = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(N)]
infected = [False] * N
infected[0] = True

queue = [0]

while queue:
    current = queue.pop(0)
    x1, y1 = positions[current]
    
    for i in range(N):
        if not infected[i]:
            x2, y2 = positions[i]
            if math.dist((x1, y1), (x2, y2)) <= D:
                infected[i] = True
                queue.append(i)

for i in range(N):
    print('Yes' if infected[i] else 'No')



'''
[問題文]
N人の人が2次元平面上にいる
人i=1が観戦した、距離がD以内にいる人にウイルスがうつる
各iについて、ウイルスに感染しているかをYesまたはNoで出力せよ

[私の考え]
・標準libでユークリッド距離計算
・BFS?

'''
