import sys

# ローカル用
# file_number =3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

def calc(l, char1, char2):
    index1 = l.index(char1)
    index2 = l.index(char2)
    return abs(index2 - index1)

p,q = input().split()
l = ['A', '', '', 'B', 'C', '', '', '', 'D', 'E', '', '', '', '', 'F', '', '', '', '', '', '', '', '', 'G']


print(calc(l,p,q))
