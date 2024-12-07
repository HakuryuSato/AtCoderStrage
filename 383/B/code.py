import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

H,W,D = map(int,input().split())
S=[]
for _ in range(H):
    S.append(list(input()))

manhattan=[]

# 案1 .ならマンハッタン距離を探索し、.の個数を数える

# 座標からマンハッタン距離のリストを生成し、その範囲を探索

# for i in range(H):
#     for j in range(W):
#         if S[i,j]=='.':
            

manhattan_list=[]
for i in range(D+1):
    for j in range(D+1-i):
        manhattan_list.append((i,j))

manhattan_list
