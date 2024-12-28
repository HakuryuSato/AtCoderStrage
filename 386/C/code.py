import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

K = int(input())
S = list(input())
T = list(input())

lenS = len(S)
lenT = len(T)

if abs(lenS - lenT) > 1:
    print("No")
    exit()

if lenS > lenT:
    S, T = T, S

i = j = diff_count = 0

while i < lenS and j < lenT:
    if S[i] == T[j]:
        i += 1
        j += 1
    else:
        diff_count += 1
        if diff_count > 1:
            print("No")
            exit()
        if lenS == lenT:
            i += 1
            j += 1
        else:
            j += 1

print("Yes" if diff_count <= 1 else "No")