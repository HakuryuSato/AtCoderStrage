import sys
import math

# ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__



s_x, s_y, e_x, e_y, T, V = map(int, input().split())
n = int(input())

max_distance = T * V

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

for i in range(n):
    x, y = map(int, input().split())
    distance_to_girl = euclidean_distance(s_x, s_y, x, y)
    distance_to_end = euclidean_distance(x, y, e_x, e_y)
    if distance_to_girl + distance_to_end <= max_distance:
        print("YES")
        break
else:
    print("NO")
