import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__


def calc(point1, point2, D):
    a, b = point1
    c, d = point2
    distance_squared = (a - b) ** 2 + (c - d) ** 2
    return distance_squared <= D ** 2
    

# N人数,D範囲
N, D = map(int, input().split())
l = [0] * N

for i in range(N):
    if(i==0):
        infected = list(map(int, input().split()))
        print('Yes')
    else:
        point = list(map(int, input().split()))
        




