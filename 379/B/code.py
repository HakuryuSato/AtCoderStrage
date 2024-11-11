import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,K=map(int,input().split())
S=list(input())

result=0
tooth_count=0
for c in S:
    if(c=='O'):
        tooth_count+=1
        if(tooth_count==K):
            result+=1
            tooth_count=0
    else:
        tooth_count=0

print(result)