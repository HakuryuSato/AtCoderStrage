import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

x=int(input())

l=[]
for i in range(1,10):
    for j in range(1,10):
        l.append(i*j)

result=0
for num in l:
    if num==x:
        continue
    else:
        result+=num

print(result)