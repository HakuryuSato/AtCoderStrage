import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# 提出用
sys.stdin = sys.__stdin__

s=input()

s= s.replace('0','2')
s=s.replace('1','0')
s=s.replace('2','1')

print(s)