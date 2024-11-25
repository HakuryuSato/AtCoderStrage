import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N = int(input())
S_input = input()


def rle(S_input):
    count = 1
    rle_list = []
    for i in range(0, len(S_input) - 1):
        if S_input[i] == S_input[i + 1]:
            count += 1
        else:
            rle_list.append((S_input[i], count))
            count = 1
    rle_list.append((S_input[-1], count))
    return rle_list

S = rle(S_input)

max_count = 0
for i in range(len(S)):
    if S[i][0] == "/":
        if (i > 0 and i < len(S) - 1) and S[i - 1][0] == "1" and S[i + 1][0] == "2":
            min_count = min(S[i - 1][1], S[i + 1][1])
            current_max = 1 + 2 * min_count
            if current_max % 2 == 0:
                current_max -= 1
            max_count = max(max_count, current_max)
        else:
            max_count = max(max_count, 1)

if S_input=='/' or max_count>1:
    print('Yes')
else:
    print('No')
