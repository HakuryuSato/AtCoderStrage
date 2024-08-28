import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N, M = map(int, input().split())
l = [set() for _ in range(N)]  # set型のリストに変更

for i in range(M):
    text = list(map(int, input().split()))
    for j, num in enumerate(text):
        l[num - 1].add(text[j - 2])  # setに追加する場合はaddを使用
        l[num - 1].add(text[j])

count = sum(1 for s in l for x in s if x < M)  # Mより小さい数の個数を数える

print(count)


