import sys
from itertools import permutations

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
P=list(map(int,input().split()))

# 全探索は100!となるため無理
# permed_P=sorted(list(permutations(P)))
# print(*permed_P[permed_P.index(tuple(P))-1])

j = N-2
while P[j]<P[j+1]:
    j-=1

k = N - 1
while P[j] < P[k]:
  k -= 1

P[j], P[k] = P[k], P[j]
print(*P[:j + 1], *P[:j:-1])