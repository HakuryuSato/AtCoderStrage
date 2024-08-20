import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())

items = [0] * N
for i in range(N):
    items[i] = list(map(int, input().split()))


# 全探索でもいい


def check(items, N, M):
    for i in range(N):
        for j in range(N):
            if i != j:
                price_i, count_i, *features_i = items[i]
                price_j, count_j, *features_j = items[j]

                if price_i >= price_j and all(f in features_j for f in features_i):
                    if price_i > price_j or len(features_j) > len(features_i):
                        return "Yes"
    return "No"


print(check(items, N, M))
