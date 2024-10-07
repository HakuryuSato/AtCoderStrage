import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
l=[1,2,3,4,5,6]

for i in range(N % 30):
    index1 = (i % 5)
    index2 = (i % 5) + 1
    l[index1], l[index2] = l[index2], l[index1]

print(''.join(map(str, l)))

'''
[問題文]
N=1~10^9

i=0~Nまでループし
左から(i%5)+1番目にあるカードと、左から(i%5)+2番目にあるカードの位置を入れ替える

最終的なlの内容を出力せよ

[私の考え]
10^9すべて処理をするのは難しい？
lのlenが小さいので、全て計算しなくても結果が出せる？
5で割ったあまりを使うことが特徴？最初に5で割ってしまえば、数回の操作で完了できるか？

'''