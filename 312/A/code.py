import sys

# # ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


S = input()

l = "ACE","BDF","CEG","DFA","EGB","FAC","GBD"

if S in l:
    print('Yes')
else:
    print('No')


