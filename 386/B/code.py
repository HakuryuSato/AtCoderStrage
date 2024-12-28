import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

S = input()


def run_length_encoding(S):
    r, c = [], 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            c += 1
        else:
            r.append((S[i - 1], c))
            c = 1
    return r + [(S[-1], c)]


encoded_S = run_length_encoding(S)

count = 0

for s in encoded_S:
    if s[0] == "0":
        count += s[1] // 2
        count += s[1] % 2
    else:
        count+=s[1]

print(count)