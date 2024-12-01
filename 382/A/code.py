import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

n, d = map(int, input().split())
s = input()
a = 0
for c in s:
    if c == '@':
        a += 1
print(n - a + d)
