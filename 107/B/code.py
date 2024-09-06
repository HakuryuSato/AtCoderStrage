import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

H, W = map(int, input().split())
l = []

for i in range(H):
    text = list(input())
    if all(cell == '.' for cell in text):
        continue
    else:
        l.append(text)

transposed_l = list(zip(*l))
filtered_transposed_l = [row for row in transposed_l if not all(cell == '.' for cell in row)]
filtered_l = list(zip(*filtered_transposed_l))

for row in filtered_l:
    print("".join(row))
