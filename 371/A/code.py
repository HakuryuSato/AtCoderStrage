import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

S=list(input().split()) # "< < <"

# 二番目に年上は誰？



if S == ['<', '<', '<'] or S == ['>', '>', '>'] or S == ['<', '>', '<'] or S == ['>', '<', '>']:
    print('B')  
elif S == ['<', '<', '>'] or S == ['>', '>', '<']:
    print('C') 
else:
    print('A')  
    