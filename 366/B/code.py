import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


N = int(input())

S = []

for i in range(N):
    S.append(input())

max_len = max(len(line) for line in S)

output_lines = []
for i in range(max_len):
    new_line = ''.join(line[i] if i < len(line) else '*' for line in reversed(S))
    new_line = new_line.rstrip('*')
    output_lines.append(new_line)


for text in output_lines:
    print(text)
