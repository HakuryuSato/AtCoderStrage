import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

box_weights = defaultdict(list)
for a, w in zip(A, W):
    box_weights[a].append(w)

move_box_weights = 0
for weights in box_weights.values():
    if len(weights) > 1:
        weights.sort()
        move_box_weights += sum(weights[:-1])

print(move_box_weights)

