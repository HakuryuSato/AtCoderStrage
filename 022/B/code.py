import sys
from collections import defaultdict

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


N = int(input().strip())
A = list(map(int, sys.stdin.read().split()))

flower_count = defaultdict(int)
for flower in A:
    flower_count[flower] += 1

pollination_count = 0
for count in flower_count.values():
    if count >= 2:
        pollination_count += (count - 1)

print(pollination_count)



'''
問題文
N個の花を訪れた(1~10^5)
A[i] 花の種類
i番目の花はi>jかつ、iとjの花の種類が同じなら受粉
->同じ値が2つ以上あれば、その数をカウント
3->2個受粉

私の考え
辞書作成して数をカウント、最後に2つ以上のデータから、-1した結果を合計
出力
'''