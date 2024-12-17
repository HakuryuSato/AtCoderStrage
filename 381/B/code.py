import sys
from collections import Counter

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

S = input()


if len(S) % 2 != 0:
    print("No")
    exit()

is_valid_pair = all(S[i] == S[i+1] for i in range(0, len(S), 2))


char_count = Counter(S)
is_valid_count = all(v == 2 for v in char_count.values())

print("Yes" if is_valid_pair and is_valid_count else "No")