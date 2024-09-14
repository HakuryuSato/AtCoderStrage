import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())  # 村の数 4 (1~2*10^5)
X = list(map(int, input().split()))  # 座標 1 3 5 7 (-10^9~10^9)
P = list(map(int, input().split()))  # 村人数 1 2 3 4 (1~10^9)
Q = int(input())  # クエリ数 4 (1~2*10^5)


# 座標が大きいので検索用
def binary_search(arr,target,is_high):
    left,right = 0,len(arr)

    while left < right:
        mid=(left+right)//2
        if is_high: 
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
    # 検索終了
    return left



# 累積和
villages = sorted(zip(X, P))
sorted_X = [v[0] for v in villages]

cum_sum = [0] * (N + 1)
for i in range(1, N + 1):
    cum_sum[i] = cum_sum[i - 1] + villages[i - 1][1]


    
for _ in range(Q): # 2*10^5 = 最大10万
    L, R = map(int, input().split()) # 検索範囲 座標L以上、R以下の人数総数を求める
    left_idx = binary_search(sorted_X, L, True)
    right_idx = binary_search(sorted_X, R, False) - 1

    # 範囲に該当する村が存在する場合、人数の総和を計算
    if left_idx <= right_idx:
        total_population = cum_sum[right_idx + 1] - cum_sum[left_idx]
    else:
        total_population = 0  # 該当する村がない場合

    print(total_population)