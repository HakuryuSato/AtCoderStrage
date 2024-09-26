import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


N, L = map(int, input().split())
strings = [input().strip() for _ in range(N)]

strings.sort()

print(''.join(strings))


