import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())

# 頂点番号を合わせるために、0を追加して調整する
# 0 6 7 2...となる
A = list(map(int, ("0 " + input()).split())) 


# 頂点1から開始
now = 1 

# now(頂点番号) = A[頂点番号] となり、頂点数分移動できる
for _ in range(N): now = A[now] # 予めN回移動する

# なぜ頂点数分移動するのか？
# N 回移動すれば必ず何らかの閉路に到達することが保証されているから


B = [now]

# 最初に発見した閉路の頂点をすべてリスト B に追加する
while B[0] != A[now]:
	now = A[now]
	B.append(now)
	
print(len(B))
print(*B)