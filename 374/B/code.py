import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

s = input()
t = input()

if s == t:
    print("0")
else:
    min_length = min(len(s), len(t))
    for i in range(min_length):
        if s[i] != t[i]:
            print(i + 1)
            break
    else:
        print(min_length + 1)
