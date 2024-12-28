import sys
from collections import defaultdict
# ローカル用
# file_number = 5
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

cards = list(map(int,input().split()))

dic = defaultdict(int)

for card in cards:
    dic[card]+=1

counts = sorted(list(dic.values()))

if counts==[1,3] or counts==[2,2]:
    print('Yes')
else:
    print('No')