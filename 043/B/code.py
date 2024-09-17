import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

s=input()

result = []
for char in s:
    if char == "0":
        result.append("0")
    elif char == "1":
        result.append("1")
    elif char == "B":
        if result:
            result.pop()

print("".join(result)) 