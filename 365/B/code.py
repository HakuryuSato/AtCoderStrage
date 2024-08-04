import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
second = sorted_a[1]
second_largest_index = a.index(second)

print(second_largest_index + 1)


