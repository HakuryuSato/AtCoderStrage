import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# 本番用
sys.stdin = sys.__stdin__


def is_palindrome(sub):
    return sub == sub[::-1]


def check(S):
    n = len(S)
    max_length = 1

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(S[i : j + 1]):
                max_length = max(max_length, j - i + 1)
    return max_length

S = input()
print(check(S))
