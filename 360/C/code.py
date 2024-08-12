import sys

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
# sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

def get_max_box(N,A,W):
    box_weights = {}
    for i in range(N):
        if A[i] not in box_weights:
            box_weights[A[i]] = 0
        box_weights[A[i]] += W[i]
    max_weight = max(box_weights.values())
    max_weight_box = next((k for k, v in box_weights.items() if v == max_weight), None)

    return max_weight_box

# 荷物が二つ入っている箱のうち、最小のものを

weight_dict = {}
for i in range(N):
    if A[i] not in weight_dict or W[i] < weight_dict[A[i]]:
        weight_dict[A[i]] = W[i]

total_weight = sum(weight_dict.values())
print(total_weight)


print()
