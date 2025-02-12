import sys


# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

from itertools import combinations
K = int(input())

dec_numbers = []
digits = "9876543210"
for length in range(1, 11):
    for comb in combinations(digits, length):
        dec_numbers.append(int("".join(sorted(comb, reverse=True))))

dec_numbers.sort()
print(dec_numbers[K])
