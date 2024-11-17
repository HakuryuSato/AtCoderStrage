import sys
from itertools import product

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__



N,X = map(int,input().split())
l=[(tuple(map(int,input().split()))) for _ in range(N)]



dp = {0} 

for values in l:
    next_dp = set()
    for value in values:
        for current_sum in dp:
            if current_sum + value <= X:  
                next_dp.add(current_sum + value)
    dp = next_dp 


print("Yes" if X in dp else "No")





# 全探索：実行時間超過


# sums = [sum(comb) for comb in product(*l)]

# print('Yes' if X in sums else 'No')
