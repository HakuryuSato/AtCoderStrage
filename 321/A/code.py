import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


N = input()

nums = list(map(int, N))
is_yes = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

if(is_yes):
    print('Yes')
else:
    print('No')