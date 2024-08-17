import sys

# ローカル用
# file_number = 4
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


X = float(input())

result = round(X, 3)
if result == int(result):
    result = int(result)
print(result)