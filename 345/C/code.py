import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

from collections import defaultdict
S=input()
N=len(S)
ans=0

count=defaultdict(int)

for j in range(N):
  ans+=j-count[S[j]]
  count[S[j]]+=1
if max(count.values())>1:
  ans+=1
print(ans)

'''
英小文字からなる長さ2~10^6の文字列S
i<jの組を選びi<j番目の文字を入れ替える
文字列としていくつの種類があり得るかを出力

[私の考え]
・出現するアルファベットの数を数える
・アルファベットの桁を数える
・組み合わせの個数を計算？


'''