import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
c = input()

r_count = c.count('R')
left_part = c[:r_count]

w_in_left = left_part.count('W')

print(w_in_left)




'''
N=医師の個数2~2*10^5
c=RまたはWの連続からなる文字列

'WR'となる部分がないように以下どちらかの操作を行う最小の回数を答えよ
・2個の文字の位置を変える
・文字1個を変える(W->R R->W)

私の考え
・うまく入れ替えが可能ならば、入れ替えのほうが手順が少なく、文字を変更するのは回数が増える
・WRを探し、偶数個？なら入れ替え？（でも入れ替えた後にWRが生まれるリスクもある？入れ替える前に調べる必要がある？
'''