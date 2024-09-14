import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input()) 
X = list(map(int, input().split()))  
P = list(map(int, input().split()))  
Q = int(input()) 


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
    return left




villages = sorted(zip(X, P))
sorted_X = [v[0] for v in villages]

cum_sum = [0] * (N + 1)
for i in range(1, N + 1):
    cum_sum[i] = cum_sum[i - 1] + villages[i - 1][1]


    
for _ in range(Q): # 2*10^5 = 最大10万
    L, R = map(int, input().split()) 
    left_idx = binary_search(sorted_X, L, True)
    right_idx = binary_search(sorted_X, R, False) - 1


    if left_idx <= right_idx:
        total_population = cum_sum[right_idx + 1] - cum_sum[left_idx]
    else:
        total_population = 0 

    print(total_population)