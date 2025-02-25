import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


S = list(input())

i = 0
while i < len(S) - 1:
    streak = 0
    if S[i] == "W" and S[i + 1] == "A":
        S[i] = "A"
        S[i + 1] = "C"

        if i > 0:
            i -= 1
    else:
        i += 1

print(''.join(S))


