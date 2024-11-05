import sys
from itertools import product

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N,M=map(int,input().split())
ab = [tuple(input().split()) for _ in range(M)]
K=int(input())
cd = [tuple(input().split()) for _ in range(K)]

max_count = 0

# 全ての配置パターンを試す
for balls in product([0, 1], repeat=K):
    placed = set()
    for i in range(K):
        if balls[i] == 0:
            placed.add(cd[i][0])
        else:
            placed.add(cd[i][1])
    
    # 条件を満たす数をカウント
    count = sum(1 for a, b in ab if a in placed and b in placed)
    
    # 最大値を更新
    max_count = max(max_count, count)

print(max_count)


'''
[問題文]
ab=条件、ボールが両方に置かれている時満たされる
cd=cまたはdどちらか一方にボールを置く
満たされる最大の条件数を出力

入力例
4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3



[私の考え]
・cdで同じ数字に置かないようにする？
・abの数字で出現回数が多いものを調べる？
・該当の数字をcdから探し、優先して選択？
・数が小さいので全探索？

'''