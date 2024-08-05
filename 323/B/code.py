import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())

lines=N*[0]
for i in range(N):
    lines[i] = [[i+1],[input().count('o')]]

sorted_data = sorted(lines, key=lambda x: x[1], reverse=True)
result = ' '.join(str(item[0][0]) for item in sorted_data)
print(result)