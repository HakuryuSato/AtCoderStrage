import sys

# ローカル用
file_number = 1 
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N,X = map(int,input().split())
l=[]

for i in range(N):
    l.append(list(map(int,input().split())))

l


sum_combinations = []

# 全ての組み合わせを生成するループ
for i in len(l[0]):
    sum=0
    for j in len(l):
        sum += 

        




            


if(X in sum_combinations):
    print('Yes')
else:
    print('No')
