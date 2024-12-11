import sys
from bisect import bisect_left
import heapq

# ローカル用
file_number = 1
sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
# sys.stdin = sys.__stdin__

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people=sorted((A[i], i+1) for i in range(N))
sushi=sorted((B[j], j+1) for j in range(M))

res=[-1]*(M)
heap=[]
p=0

for bj, sj in sushi:
    # A_i ≤ bj となる人を全てヒープに追加
    while p<N and people[p][0]<=bj:
        # ヒープには人の番号(i)で管理(人番号が小さい順に取り出せるように)
        heapq.heappush(heap, people[p][1])
        p+=1
    
    if heap:
        # 最も人番号が小さい人がこの寿司を取る
        i=heap[0]  # ヒープから取り出さない(人は何度でも取れる)
        res[sj-1]=i
    else:
        # 誰も取らない
        res[sj-1]=-1

print("\n".join(map(str,res)))





"""
[メモ]
AまたはBのどちらかでループ？
人のインデックスを保持したまま、美食度と対応した辞書か配列を作る
二分探索か、

"""
