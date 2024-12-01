import sys
from heapq import heappush, heappop

# ローカル用
file_number = 2
sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
# sys.stdin = sys.__stdin__

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people = sorted((A[i], i + 1) for i in range(N))
sushi = sorted((B[j], j) for j in range(M)) 

result = [-1] * M
available = []
person_idx = 0

for b, sushi_idx in sushi:
    while person_idx < N and people[person_idx][0] <= b:
        heappush(available, people[person_idx])
        person_idx += 1
    
    if available:
        _, person_number = heappop(available)
        result[sushi_idx] = person_number

print('\n'.join(map(str, result)))










"""
[メモ]
maxを作成してmax以下なら-1？
ただそれだと10^10探索
辞書を使う？
二分探索は？->順番だから無理か？

辞書にしたうえで昇順にソートしておけば？


"""

