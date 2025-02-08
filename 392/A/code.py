import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

l = list(map(int,input().split()))

l.sort()



if(l[0]*l[1]==l[2]):
    print('Yes')
else:
    print('No')