import sys
from collections import Counter

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N=int(input())
s = [Counter(input()) for _ in range(N)]

common_chars = s[0].keys()
for i in range(1, N):
    common_chars &= s[i].keys()

result = []
for char in common_chars:
    min_count = min(c[char] for c in s)
    result.extend([char] * min_count)

print("".join(sorted(result)))





'''
実行時間2秒 メモリ1GB
[問題文]
文字列がn(1~50)個与えられる
n個の文字列全てに含まれる部分文字列のうち、
最長のものを辞書順で出力せよ

入力例
3
cbaa
daacc
acacac


出力例
aac


[私の考え]
・辞書を作成して

'''