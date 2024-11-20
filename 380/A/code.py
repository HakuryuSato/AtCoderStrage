import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


N=input()

print('Yes' if N.count('1')==1 and N.count('2')==2 and N.count('3')==3 else 'No')